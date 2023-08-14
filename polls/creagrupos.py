#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para la inyección de datos
from .models import RelExpedienteCurp,Grupo,Negocio,Expediente,Creditos,RelExpedienteCredito,Cursos
#Llamado de modelos para referencias
from .models import TipoGrupo,Solicitantes,TiposCredito
#Biblioteca para imprimir en terminal
import logging
#Biblioteca para tratar el dato de la fecha
from datetime import datetime
#biblioteca para convertir la respuesta a json utf-8
import json
#biblioteca para generar el hash
import hashlib

logger = logging.getLogger(__name__)
#genera hash
def generar_hash(password):
    # Calcular el hash utilizando SHA-256
    hash_obj = hashlib.sha256(password.encode())
    # Obtener la representación en hexadecimal del hash
    hash_resultado = hash_obj.hexdigest()    
    return hash_resultado
#Genera expediente
def generar_expediente(variable1, tipo_grupo, miembros, variable2):
    # Obtener las primeras 4 letras de la variable1
    primeras_letras = variable1[:4]
    # Obtener el tipo de grupo (I o G)
    tipo_grupo_letra = 'I' if tipo_grupo == 1 else 'G'
    # Asegurarse de que el número de miembros esté dentro del rango (2 a 5)
    miembros = max(2, min(miembros, 5))
    # Obtener el mes y la fecha actual en el formato ddmmaa
    fecha_actual = datetime.now().strftime('%d%m%y')
    # Obtener las primeras 4 letras de la variable2
    ultimas_letras = variable2[:4]
    # Combinar todos los elementos para formar la clave de identificación
    clave_identificacion = f'EXP-{primeras_letras}{tipo_grupo_letra}{miembros}{fecha_actual}{ultimas_letras}'
    return clave_identificacion

@csrf_exempt
def CrearGrupos(request):
    if request.method == 'POST':
        logger.info('Este es un mensaje en donde se crea los grupos')
        body = json.loads(request.body.decode('utf-8'))
        #logger.debug(body)
        try:            
            miembros                    =int(body['members'])
            nombre_grupo                =body['namegroup']
            tipo_grupo                  =TipoGrupo.objects.get(tipo_grupo_id=int(body['typegroup']))
            inttipo_grupo               =int(body['typegroup'])
            tipo_credito_solicitado     =TiposCredito.objects.get(tipo_credito_id=int(body['idtypecredit']))
            fecha_de_solicitud          = datetime.today().strftime('%Y-%m-%d')
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #valida los miembros sean minimo 2 y maximo 5
        if miembros < 2 or miembros > 5:            
            return JsonResponse({'error': 'Número de miembros inválido'}, status=400)
        #crea una lista con los solicitantes de credito
        try:
            curp_list = [Solicitantes.objects.get(curp=body[f'curp{i}']) for i in range(1, miembros + 1)]
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        
        #candado para validar si no hay usuarios en otro proceso de credito
        for curp_obj in curp_list:
            if RelExpedienteCurp.objects.filter(curp=curp_obj, activo=True).exists():
                logger.info('Al menos un registro ya está activo.')
                return JsonResponse({'error': 'Al menos un registro ya está activo.'}, status=400)

        #NUEVO EXPEDIENTE
        expediente=generar_expediente(body['curp1'],inttipo_grupo,miembros,body['curp2'])
        hashexp = generar_hash(expediente)
        nuevo_expediente = Expediente(expediente=expediente,hash_expediente=hashexp)
        nuevo_expediente.save()
        #Obtengo el Id de mi nuevo expediente
        expediente_id = nuevo_expediente.expediente_id
        expediente_id_busqueda= Expediente.objects.get(expediente_id=expediente_id)
        contador = 0
        #NUEVO GRUPO
        nuevo_grupo = Grupo(nombre_grupo=nombre_grupo,tipo_grupo=tipo_grupo)
        nuevo_grupo.save()
        #Obtengo el Id de mi nuevo grupo
        grupo_id = nuevo_grupo.grupo_id
        grupo_id_busqueda= Grupo.objects.get(grupo_id=grupo_id)
        #NUEVO CREDITO
        nuevo_credito = Creditos(tipo_credito_solicitado=tipo_credito_solicitado,fecha_solicitud=fecha_de_solicitud)
        nuevo_credito.save()
        #Obtengo el Id de mi nuevo grupo
        credito_id = nuevo_credito.credito_id
        credito_id_busqueda= Creditos.objects.get(credito_id=credito_id)
        #NUEVA REL_EXPEDIENTE_CREDITO
        nuevo_exp_cred = RelExpedienteCredito(expediente=expediente_id_busqueda,credito=credito_id_busqueda)
        nuevo_exp_cred.save()
        #Obtengo el Id de mi nuevo grupo
        exp_cred_id = nuevo_exp_cred.rel_expediente_credito_id
        exp_cred_id_busqueda= RelExpedienteCredito.objects.get(rel_expediente_credito_id=exp_cred_id)
        for solicitante in curp_list:
            # Incrementar el contador en 1 para cada objeto iterado
            contador += 1
            # Determinar si es el primer objeto y establecer es_obligado_solidario en True o False
            if inttipo_grupo == 1:
                es_obligado_solidario = True if contador == 2 else False
                es_representante = False
            if inttipo_grupo == 2:
                es_representante = True if contador == 1 else False
                es_obligado_solidario = False
            # Crear y guardar el registro en RelExpedienteCurp
            nuevo_rel_expediente_curp = RelExpedienteCurp(expediente=expediente_id_busqueda, grupo=grupo_id_busqueda,curp=solicitante ,es_obligado_solidario=es_obligado_solidario,es_representante=es_representante,secuencial=contador,activo=True)
            nuevo_rel_expediente_curp.save()
            #Crea el regitro de cursos
            nuevo_curso = Cursos(credito=credito_id_busqueda,curp=solicitante)
            nuevo_curso.save()
        
        return JsonResponse({'mensaje': 'Datos insertados exitosamente.'})
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)
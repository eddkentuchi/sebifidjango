#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para la inyección de datos
from .models import Solicitantes
#llamado de modelos para busqueda de usuarios
from .models import RelDireccionCurp,RelExpedienteCurp,RelExpedienteCredito,Creditos,Cursos
#Biblioteca para imprimir en terminal
import logging
#biblioteca para convertir la respuesta a json utf-8
import json
#biblioteca para generar el hash
import hashlib
#busquedas compuestas
from django.db.models import Q
#biblioteca para generar el random
import random

logger = logging.getLogger(__name__)
#genera hash
def generar_hash(password):
    logger.debug(password)
    # Calcular el hash utilizando SHA-256
    hash_obj = hashlib.sha256(password.encode())
    # Obtener la representación en hexadecimal del hash
    hash_resultado = hash_obj.hexdigest()    
    return hash_resultado

#Metodo post para el formulario de registro
@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info('Este es el random')
        logger.debug(body)
        try:
            email               =body['email']
            contraseña          =body['password']
            myhash = generar_hash(contraseña)
            logger.debug(myhash)
            #estado_id = int(body.get('IdEstado'))
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        registros = Solicitantes.objects.filter(email=email) 

        if registros.exists():
        # Se encontraron registros que cumplen al menos una de las condiciones
            if registros.filter(hash=myhash).exists():
                logger.debug(registros)
                # Se encontraron registros que cumplen ambas condiciones
                resp_list = [{'curp': registro.curp} for registro in registros]
                return JsonResponse(list(resp_list), safe=False)
                
            else:
                # Se encontró el email, pero no la password
                error_msg1 = {'error': 'Contraseña incorrecta'}                
                return JsonResponse([error_msg1],safe=False, status=200)
        else:
            #No se encontro usuario
            error_msg2 = {'error': 'Usuario no encontrado'}
            return JsonResponse([error_msg2],safe=False, status=200)
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

#Metodo para recuperar usuario
@csrf_exempt
def recuperaUsuario(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info('Este es el random')
        logger.debug(body)
        try:
            curp                =body['curp'].upper()
            primer_apellido     =body['firstlastname'].upper()
            segundo_apellido    =body['secondlastname'].upper()
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        registros = Solicitantes.objects.filter(Q(curp=curp) & Q(primer_apellido=primer_apellido)& Q(segundo_apellido=segundo_apellido)) 

        if registros.exists():
        # Se encontraron registros que cumplen con la condicion
            
            resp_list = [{'email': registro.email} for registro in registros]
            logger.debug(resp_list)
            return JsonResponse(list(resp_list), safe=False)
            
        else:
            error_msg2 = {'error': 'Usuario no encontrado'}
            return JsonResponse([error_msg2],safe=False, status=200)
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

#Metodo para recuperar contraseña
@csrf_exempt
def recuperaContrase(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info('Este es el random')
        logger.debug(body)
        try:
            curp      =body['curp'].upper()
            email     =body['email']
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        registros = Solicitantes.objects.filter(Q(curp=curp) & Q(email=email)) 

        if registros.exists():
            # Se encontraron registros que cumplen con la condicion
            #aleatorio
            registro = registros.first()
            numero_aleatorio = random.randint(10000000, 99999999)
            # Convertir el número a cadena de texto
            numero_aleatorio_str = str(numero_aleatorio)
            myhash = generar_hash(numero_aleatorio_str)

            logger.info('Este es mi hash')
            logger.debug(myhash)
            logger.info('Este es el random')
            logger.debug(numero_aleatorio)
            
            registro.hash = myhash
            registro.save()
            return JsonResponse([{'mensaje': 'Datos insertados exitosamente.'}], safe=False)
            
        else:
            error_msg2 = {'error': 'Usuario no encontrado'}
            return JsonResponse([error_msg2],safe=False, status=200)
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

    #Metodo para recuperar usuario

#Metodo para buscar si usuario ya tiene una dirección
@csrf_exempt
def UserWithDir(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info('Este es el random')
        logger.debug(body)
        try:
            curp                =body['curp'].upper()
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        registros = RelDireccionCurp.objects.filter(curp=curp) 

        if registros.exists():
        # Se encontraron registros que cumplen con la condicion
            
            resp_list = [{'idDir': registro.rel_direccion_curp_id} for registro in registros]
            logger.debug(resp_list)
            return JsonResponse(list(resp_list), safe=False)
            
        else:
            logger.info('No hay direccion de usuario')
            return JsonResponse({'error': 'No hay registro de direccion'}, status=400)
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

#Metodo para recuperar contraseña
@csrf_exempt
def DatosUsuario(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.info('Este es el random')
        logger.debug(body)
        try:
            curp      =body['curp'].upper()
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        solicitante = Solicitantes.objects.get(curp=curp)
        #solicitante = [{'name': respuesta['nombre'],'firstlastname' : respuesta['primer_apellido'],'secondlastname' : respuesta['segundo_apellido'],'folio' : respuesta['folio']} for respuesta in solicitantes]
        resp_list = []
        statusvalue = 0
        if solicitante.folio is None:
            statusvalue = 0
        else:
            try:
                rels_exp_curp=RelExpedienteCurp.objects.get(curp=curp, activo=True)
                logger.debug(rels_exp_curp)
            except RelExpedienteCurp.DoesNotExist:
                statusvalue = 1
                resp_list.append({
                'name':             solicitante.nombre,
                'firstlastname':    solicitante.primer_apellido,
                'secondlastname':   solicitante.segundo_apellido,
                'folio':            solicitante.folio,
                'casevalue':        statusvalue
                })
                logger.debug(resp_list)
                return JsonResponse(list(resp_list), safe=False)
            #separo a representantes y solicitantes
            if rels_exp_curp.es_obligado_solidario == False or rels_exp_curp.es_representante == True:
                logger.info('Es el mero machin del grupo')
                if rels_exp_curp.negocio is None:
                    statusvalue= 2
                else:
                    rel_exp_credito = RelExpedienteCredito.objects.get(expediente=rels_exp_curp.expediente)
                    credito = rel_exp_credito.credito
                    creditos_obj = Creditos.objects.get(credito_id=credito.credito_id)
                    if creditos_obj.folio is None:
                        statusvalue= 3
                    else:
                        try:
                            curso = Cursos.objects.get(Q(credito=creditos_obj.credito_id) & Q(curp=solicitante) & Q(curso_fecha__isnull=True) & Q(curso_valido__isnull=True))
                        except Cursos.DoesNotExist:
                            resp_list.append({
                            'name':             solicitante.nombre,
                            'firstlastname':    solicitante.primer_apellido,
                            'secondlastname':   solicitante.segundo_apellido,
                            'folio':            solicitante.folio,
                            'casevalue':        statusvalue
                            })
                            logger.debug(resp_list)
                            return JsonResponse(list(resp_list), safe=False)
                        statusvalue = 4    
            # cuando son obligados y miembros de grupo
            else:
                logger.info('Es un simple mortal')
                rel_exp_credito = RelExpedienteCredito.objects.get(expediente=rels_exp_curp.expediente)
                credito = rel_exp_credito.credito
                creditos_obj = Creditos.objects.get(credito_id=credito.credito_id)
                try:
                    curso = Cursos.objects.get(Q(credito=creditos_obj.credito_id) & Q(curp=solicitante) & Q(curso_fecha__isnull=True) & Q(curso_valido__isnull=True))
                except Cursos.DoesNotExist:
                    resp_list.append({
                    'name':             solicitante.nombre,
                    'firstlastname':    solicitante.primer_apellido,
                    'secondlastname':   solicitante.segundo_apellido,
                    'folio':            solicitante.folio,
                    'casevalue':        statusvalue
                    })
                    logger.debug(resp_list)
                    return JsonResponse(list(resp_list), safe=False)
            statusvalue = 4   
        #si no encuentra nada me dice que no tiene ningun credito y puede solicitar uno
        resp_list.append({
            'name':             solicitante.nombre,
            'firstlastname':    solicitante.primer_apellido,
            'secondlastname':   solicitante.segundo_apellido,
            'folio':            solicitante.folio,
            'casevalue':        statusvalue
        })
        logger.debug(resp_list)
        return JsonResponse(list(resp_list), safe=False)
            
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

    #Metodo para recuperar usuario


#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para la inyección de datos
from .models import Solicitantes,Direcciones,RelDireccionCurp
#Llamado de modelos para referencias
from .models import Sexo,TipoPoblacion,Etnia,EstadoCivil,Colonias
#Biblioteca para imprimir en terminal
import logging
#Biblioteca para tratar el dato de la fecha
from datetime import datetime
#biblioteca para convertir la respuesta a json utf-8
import json
#biblioteca para generar el hash
import hashlib
import random


logger = logging.getLogger(__name__)
#genera hash
def generar_hash():
    #aleatorio
    numero_aleatorio = random.randint(10000000, 99999999)
    # Convertir el número a cadena de texto
    numero_aleatorio_str = str(numero_aleatorio)
    # Calcular el hash utilizando SHA-256
    hash_obj = hashlib.sha256(numero_aleatorio_str.encode())
    # Obtener la representación en hexadecimal del hash
    hash_resultado = hash_obj.hexdigest()
    return hash_resultado, numero_aleatorio
#me comvierte la fecha para guardarlo bn el la bd
def convertir_formato_fecha(fecha):
    try:
        
        fecha_objeto = datetime.strptime(fecha, "%d/%m/%y")        
        # Obtener el año actual
        year_actual = datetime.now().year        
        # Obtener el año de la fecha de entrada
        year_entrada = fecha_objeto.year                
        # Establecer la lógica de autocompletar el año
        if year_entrada > year_actual:
            year_auto_completado = year_entrada -100
        else:
            year_auto_completado = year_entrada        
        # Actualizar el año en el objeto de fecha
        fecha_objeto = fecha_objeto.replace(year=year_auto_completado)
        fecha_formateada = fecha_objeto.strftime("%Y-%m-%d")
        return fecha_formateada
    except ValueError:
        raise ValidationError('El formato de fecha es inválido. Debe ser dd/mm/aa.')

#Metodo post para el formulario de registro
@csrf_exempt
def Userdata(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        myhash, numero_aleatorio = generar_hash()
        logger.info('Este es mi hash')
        logger.debug(myhash)
        logger.info('Este es el random')
        logger.debug(numero_aleatorio)
        try:
            curp                  =body['curp']
            nombre                =body['name']
            primer_apellido       =body['firstlastname']
            segundo_apellido      =body['secondlastname']
            telefono              =body['phonenumber']
            email                 =body['email']
            fecha_convertida = convertir_formato_fecha(body['birthdate'])
            fecha_nacimiento      =fecha_convertida
            sexo                  =Sexo.objects.get(sexo_id=int(body['sex']))
            estado_civil          =EstadoCivil.objects.get(estado_civil_id=int(body['civilstatus']))
            tipo_poblacion        =TipoPoblacion.objects.get(tipo_poblacion_id=int(body['typepolulation']))
            grupo_vulnerable      =False
            grupo_prioritario     =False
            etnia                 =Etnia.objects.get(etnia_id=int(body['ethnicity']))
            identificacion_oficial='uno'
            numero_identificacion ='dos'
            nacionalidad          =body['nacionality']
            hash                  =myhash
            #estado_id = int(body.get('IdEstado'))
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #crea el objeto que se inyectara en la bd
        nuevo_objeto = Solicitantes(curp=curp, nombre=nombre,primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,telefono=telefono,email=email,fecha_nacimiento=fecha_nacimiento,sexo=sexo,estado_civil=estado_civil,tipo_poblacion=tipo_poblacion,grupo_vulnerable=grupo_vulnerable,grupo_prioritario=grupo_prioritario,etnia=etnia,identificacion_oficial=identificacion_oficial,numero_identificacion=numero_identificacion,nacionalidad=nacionalidad,hash=hash)
        nuevo_objeto.save()
        return JsonResponse({'mensaje': 'Datos insertados exitosamente.'})
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

#Metodo post para el formulario
@csrf_exempt
def Userdataddress(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        if 'internalnumber' in body:            
            num_interior            =body['internalnumber']
        else:
            num_interior            =''
        if 'phonenumber' in body:            
            telefono_fijo            =body['phonenumber']
        else:
            telefono_fijo            =''
        try:            
            alias                   =body['alias']
            calle                   =body['street']
            num_exterior            =body['externalnumber']
            colonia                 =Colonias.objects.get(colonia_id=int(body['colony']))
            entre_calles            =body['streetsaround']
            referencia_domicilio    =body['references']
            editable                =0
            logger.debug(body['curp'])
            curp                    =Solicitantes.objects.get(curp=body['curp'])
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #crea el objeto que se inyectara en la bd  en el modelo Direccciones
        nuevo_objeto = Direcciones(alias=alias, calle=calle,num_exterior=num_exterior,num_interior=num_interior,colonia=colonia,telefono_fijo=telefono_fijo,entre_calles=entre_calles,referencia_domicilio=referencia_domicilio,editable=editable)
        nuevo_objeto.save()
        #Obtengo el Id de mi nuevo objeto
        direccion_id = nuevo_objeto.direccion_id
        # Obtener la instancia de Direcciones correspondiente al ID
        direccion_id_busqueda= Direcciones.objects.get(direccion_id=direccion_id)
        #crea el objeto2 que se inyectara en la bd en el modelo RelDireccionCur
        nuevo_objeto2 = RelDireccionCurp(curp=curp,direccion=direccion_id_busqueda,fecha_vigencia='2023-07-22')
        nuevo_objeto2.save()
        return JsonResponse({'mensaje': 'Datos insertados exitosamente.'})
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)
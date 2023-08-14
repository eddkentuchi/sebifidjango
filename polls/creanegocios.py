#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para la inyección de datos
from .models import Negocio,RelDireccionNegocio
#Llamado de modelos para referencias
from .models import Solicitantes,Giros,Direcciones,RelExpedienteCurp
#Biblioteca para imprimir en terminal
import logging
#Biblioteca para tratar el dato de la fecha
from datetime import datetime
#biblioteca para convertir la respuesta a json utf-8
import json
#biblioteca para generar el hash
import hashlib

logger = logging.getLogger(__name__)

@csrf_exempt
def CrearNegocios(request):
    if request.method == 'POST':
        logger.info('Este es un mensaje de depuración')
        body = json.loads(request.body.decode('utf-8'))
        
        try:
            miembros                    =int(body['members'])
            #variables de negocio
            denominacion_razon_social   =body['businessname']
            rfc                         =body['rfc']
            giro                        =Giros.objects.get(giro_id=int(body['idlineof']))
            telefono_negocio            =body['phonenumber']
            email                       =body['email']
            #variable de relacion neg dir
            direccion                   =Direcciones.objects.get(direccion_id=int(body['idAddress']))
            fecha_vigencia              =datetime.today().strftime('%Y-%m-%d')
            
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        
        try:
            curp_list = [Solicitantes.objects.get(curp=body[f'curp{i}']) for i in range(1, miembros)]
            exp_list = [RelExpedienteCurp.objects.get(rel_expediente_curp_id=body[f'idexp{i}']) for i in range(miembros)]
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        logger.debug(curp_list)
        logger.debug(exp_list)
        #NUEVO OBJETO
        nuevo_negocio = Negocio(denominacion_razon_social=denominacion_razon_social,rfc=rfc,giro=giro,telefono_negocio=telefono_negocio,email=email)
        nuevo_negocio.save()
        #Obtengo el Id de mi nuevo objeto
        negocio_id = nuevo_negocio.negocio_id
        negocio_id= Negocio.objects.get(negocio_id=negocio_id) 
        
        nuevo_rel_direccion_negocio = RelDireccionNegocio(negocio=negocio_id, direccion=direccion,fecha_vigencia=fecha_vigencia)
        nuevo_rel_direccion_negocio.save()
        
        for expediente in exp_list:
            
            expediente.negocio = negocio_id
            expediente.save()

        return JsonResponse({'mensaje': 'Datos insertados exitosamente.'})
    
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)
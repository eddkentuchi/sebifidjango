#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para consulta de datos
from .models import Solicitantes,Documentos,DocumentoRequerido,RelExpedienteCurp
#biblioteca para convertir la respuesta a json utf-8
import json
#busquedas compuestas
from django.db.models import Q
#Biblioteca para imprimir en terminal
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def ValidaCurp(request):
    logger.info('Este es un mensaje de depuración')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            curp = body['curp']
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(curp)        
        #Busqueda de las colonias asignadas
        try:
            respuesta = Solicitantes.objects.get(curp=curp)
        except:
            #No se encontro usuario
            logger.info('Este usuario no esta registrado')
            return JsonResponse([{'error': 'Usuario no encontrado','description':'Revisa que el CURP sea el correcto, si es correcto es necesario que se registrarse a la app.'}],safe=False, status=200)
        # Se encontraron registros que cumplen la condición
        if respuesta.folio is None:
            logger.info('Este usuario no tiene folio')
            return JsonResponse([{'error': 'Usuario sin folio','description':'Tu compañero no tiene folio, aún no puede solicitar un credito a el FONDESO'}],safe=False, status=200)
        else:
            logger.debug(respuesta)
            # Se encontraron registros que cumplen ambas condiciones
            if RelExpedienteCurp.objects.filter(curp=respuesta, activo=True).exists():
                logger.info('Al menos un registro ya está activo.')
                return JsonResponse([{'error': 'Usuario con crédito','description':'Este usuario no puede solicitar un nuevo credito ya tiene un credito en proceso'}],safe=False, status=200)

            resp_list =[]
            resp_list.append({
                'nombrecompleto': f"{respuesta.nombre} {respuesta.primer_apellido} {respuesta.segundo_apellido}",
                'email':    respuesta.email,
                'folio':    respuesta.folio
            })
            return JsonResponse(list(resp_list), safe=False)                    
        
    
    return JsonResponse([{'error': 'Solicitud inválida'}], status=400)

@csrf_exempt
def ValidaGenDocs(request):
    logger.info('Este es un mensaje de depuración')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            curp= body['curp']
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(curp)        
        #Busqueda de las colonias asignadas
        tipo_credito = -1
        tipo_persona = -1
        docs = DocumentoRequerido.objects.filter(tipo_credito=tipo_credito,tipo_persona=tipo_persona).values('documento_requerido_id')
        logger.debug(docs)
        respuestas = Documentos.objects.filter(Q(documento_requerido_id__in=docs) & Q(curp=curp)).values('documento_id', 'ruta_documento')
        logger.debug(respuestas)
        if respuestas.exists():
            if len(docs) == len(respuestas):
                logger.info('Se a completado el registro exitosamente')
                
                solicitante = Solicitantes.objects.get(curp=curp)
                foliouser='Folio1234'
                solicitante.folio = foliouser
                solicitante.save()
                return JsonResponse([{'mensaje': foliouser}],safe=False, status=200)
            else:
                logger.info('falta algún documento')
                return JsonResponse([{'error': 'Aún no has subido todos tus documentos'}],safe=False, status=200)
        else:
            #No se encontro usuario
            logger.info('Ningun documento encontrado')
            return JsonResponse([{'error': 'No has subido ninguno de tus documentos'}],safe=False, status=200)
    
    return JsonResponse([{'error': 'Solicitud inválida'}], status=400)

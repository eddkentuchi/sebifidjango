from django.http import JsonResponse
from .models import Colonias,Municipios,Estados,Sectores,Giros
import json
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def CodigoPostal(request):
    logger.debug('Este es un mensaje de depuración')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            codigop = body['postalcode']
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(codigop)
        if codigop:
            #Busqueda de las colonias asignadas
            respuestas = Colonias.objects.filter(codigo_postal=codigop).values('colonia_id','colonia','municipio_id')
            #resp_list = [{'idcol': respuesta['colonia_id'],'datavalue': respuesta['colonia'],'idmun':respuesta['municipio_id']} for respuesta in respuestas]
            if not respuestas:
                error_response = {'error': 'No se encontraron resultados para el código postal proporcionado.'}
                return JsonResponse(error_response, status=404)
            
            resp_list = []

            for respuesta in respuestas:
                idmun = respuesta['municipio_id']
                colonia = Colonias.objects.get(colonia_id=respuesta['colonia_id'])
                municipio = colonia.municipio
                estado_id = municipio.estado_id
                estado_nombre = municipio.estado.estado

                resp_list.append({
                    'idcol': respuesta['colonia_id'],
                    'colonia': respuesta['colonia'],
                    'idmun': idmun,
                    'municipio': municipio.municipio,
                    'idestado': estado_id,
                    'estado': estado_nombre
                })            
            logger.info('esta es mi respuesta')
            logger.debug(resp_list)
            return JsonResponse(list(resp_list), safe=False)
        else:
            logger.info('No se pudo parcear')
            return JsonResponse({'error': 'Codigo postal incorrecto'}, status=400)


@csrf_exempt
def BuscaGiros(request):
    logger.debug('Este es un mensaje de depuración')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            sector = body['sector']
            sector_id =Sectores.objects.get(sector_id=int(body['idsector'])) 
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(sector)
        if sector:
            #Busqueda de las giros asignadas
            giros = Giros.objects.filter(sector=sector_id)
            #resp_list = [{'idcol': respuesta['colonia_id'],'datavalue': respuesta['colonia'],'idmun':respuesta['municipio_id']} for respuesta in respuestas]
            if not giros:
                error_response = {'error': 'No se encontraron resultados para el código postal proporcionado.'}
                return JsonResponse(error_response, status=404)
            
            resp_list = []         
            logger.debug(giros)
            for giro in giros:
                resp_list.append({
                    'id': giro.giro_id,
                    'datavalue': giro.giro,
                })       
            logger.info('esta es mi respuesta')
            logger.debug(resp_list)
            return JsonResponse(list(resp_list), safe=False)
        else:
            logger.info('No se pudo parcear')
            return JsonResponse({'error': 'Codigo postal incorrecto'}, status=400)


#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#Llamado de modelos para referencias
from .models import TipoGrupo,Solicitantes,Grupo,Negocio,Expediente,Creditos,DocumentoRequerido
from .models import Colonias,Municipios,Estados,Sectores,Giros
from .models import RelExpedienteCredito,RelExpedienteCurp,RelDireccionCurp
from .models import TiposCredito,TipoPersona,DocumentoRequerido,Procedimientos
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
def BExpeCurp(request):
    logger.info('Este es un mensaje de depuración para busca expediente')
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
        activo = True
        grupo_valor = RelExpedienteCurp.objects.get(curp=curp,activo=activo).grupo
        logger.debug(grupo_valor) 
        # Ahora, utiliza ese grupo para obtener los registros en RelExpedienteCurp
        relexpcurp_list = RelExpedienteCurp.objects.filter(grupo=grupo_valor, activo=activo).values('curp','rel_expediente_curp_id')
        # Ahora puedes iterar sobre la lista de registros
        curps = [{'curp' + str(i): respuesta['curp'],'idexp' + str(i): respuesta['rel_expediente_curp_id'],} for i, respuesta in enumerate(relexpcurp_list)]
        
        logger.debug(curps)
        return JsonResponse(list(curps),safe=False, status=200)
        
    return JsonResponse([{'error': 'Solicitud inválida'}], status=400)

@csrf_exempt
def BDirecciones(request):
    logger.info('Este es un mensaje de depuración para busca direcciones')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        
        numero_objetos = len(body)/2
        logger.debug(numero_objetos)
        try:
            miembros  = int(body['members'])
            curp_list = [Solicitantes.objects.get(curp=body[f'curp{i}']) for i in range(miembros)]
            
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(curp_list)
        direcciones_list = []
        for solicitante in curp_list:
            # Obtener los objetos 'RelDireccionCurp' relacionados con el 'Solicitantes'
            relaciones = RelDireccionCurp.objects.filter(curp=solicitante)

            # Iterar sobre cada objeto 'RelDireccionCurp' para obtener la información de las direcciones
            for relacion in relaciones:
                direccion = relacion.direccion
                direccion_info = {
                    'direccion_id': direccion.direccion_id,
                    'alias': direccion.alias,
                    'calle': direccion.calle,
                    'num_exterior': direccion.num_exterior,
                    'num_interior': direccion.num_interior,
                    #'colonia': direccion.colonia.nombre_colonia if direccion.colonia else None,
                    #'telefono_fijo': direccion.telefono_fijo,
                    #'entre_calles': direccion.entre_calles,
                    'referencia_domicilio': direccion.referencia_domicilio,
                    #'editable': direccion.editable,
                    #'fecha_vigencia': relacion.fecha_vigencia,
                }
                direcciones_list.append(direccion_info)
        
        logger.debug(direcciones_list)
        return JsonResponse(list(direcciones_list),safe=False, status=200)
        
    return JsonResponse([{'error': 'Solicitud inválida'}], status=400)

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

@csrf_exempt
def CreditDocsList(request):
    logger.debug('Este es un mensaje de depuración')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            curp = Solicitantes.objects.get(curp=body['curp'])   
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        # Obtener el parámetro 'codigop' de la solicitud
        logger.debug(curp)
        try:
            rels_exp_curp=RelExpedienteCurp.objects.get(curp=curp, activo=True)
            logger.debug(rels_exp_curp.expediente)
            rel_exp_credito = RelExpedienteCredito.objects.get(expediente=rels_exp_curp.expediente)
            credito = rel_exp_credito.credito
            logger.debug(credito)
            creditos_obj = Creditos.objects.get(credito_id=credito.credito_id)
            tipo_credito_solicitado = creditos_obj.tipo_credito_solicitado
            logger.debug(tipo_credito_solicitado)
        except (TypeError, ValueError):
            logger.info('Error en la busqueda')
            return JsonResponse({'error': 'Error en la busqueda'}, status=400)
        #generación de la lista de docsrequeridos
        documentos_requeridos = DocumentoRequerido.objects.filter(tipo_credito=tipo_credito_solicitado)
        # Crear una lista con los datos de documentos requeridos
        resp_list = []
        for documento in documentos_requeridos:
            resp_list.append({
                'docrequired': documento.documento_requerido,
                'docrequiredhint': documento.documento_requerido_hint,
                'docrurlformat': documento.documento_requerido_url_formato,
                'docurlhelp': documento.documento_requerido_url_ayuda
            })
        logger.debug(resp_list)
        return JsonResponse(list(resp_list), safe=False)        

@csrf_exempt
def DetallesCredit(request):
    logger.debug('Este es un mensaje de depuración para detalles de los creditos')
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        logger.debug(body)
        try:
            tipo_credito_id = TiposCredito.objects.get(tipo_credito_id=body['idtype'])
            tipo_persona_id = TipoPersona.objects.get(tipo_persona_id=body['idperson'])   
          
        except (TypeError, ValueError):
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        logger.debug(tipo_credito_id)
        first_list = []
        first_list.append({
                'namecredit':   tipo_credito_id.nombre_credito,
                'objective':    tipo_credito_id.objetivo,
                'urlDirection': tipo_credito_id.tipo_credito_url,
                'pay':          tipo_credito_id.nombre_credito,
                'register':     tipo_credito_id.nombre_credito,
                'period':       tipo_credito_id.nombre_credito

            })
        try:
            documentos_requeridos = DocumentoRequerido.objects.filter(tipo_credito=tipo_credito_id,tipo_persona=tipo_persona_id)
            procedimientos=Procedimientos.objects.filter(tipo_credito=tipo_credito_id)
                     
        except (TypeError, ValueError):
            documento.info('Error en la busqueda')
            return JsonResponse({'error': 'Error en la busqueda'}, status=400)
        second_list = []
        for documento in documentos_requeridos:
            second_list.append({
                'docrequired':      documento.documento_requerido,
                'hint':  documento.documento_requerido_hint,
                'pdf':    documento.documento_requerido_url_formato,
                'web':       documento.documento_requerido_url_ayuda
            })
        third_list = []
        for procedimiento in procedimientos:
            third_list.append({
                'proceduralorder':  procedimiento.paso_orden,
                'procedural':       procedimiento.procedimiento_paso,                
                'web':    procedimiento.paso_url,
                
            })
        logger.debug(second_list)
        return JsonResponse({'first': first_list,'second': second_list,'third': third_list}, safe=False)        

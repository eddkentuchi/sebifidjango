#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#llamado de modelo solicitantes para la inyección de datos
from .models import Documentos
#Llamado de modelos para referencias
from .models import DocumentoRequerido, Solicitantes
#Biblioteca para imprimir en terminal
import logging
#biblioteca para el manejo del nombre unico de los archivos
import os
#biblioteca para el tiempo
import time
#biblioteca para convertir la respuesta a json utf-8
import json
#busquedas compuestas
from django.db.models import Q


logger = logging.getLogger(__name__)


@csrf_exempt
def Guardardocumento(request):

    if request.method == 'POST' and request.FILES['imagen']:
        imagen = request.FILES['imagen']
        body = json.loads(request.POST.get('form'))
        logger.debug(body)
        # Generar un nombre único para el archivo
        nombre_original, extension = os.path.splitext(imagen.name)
        nombre_archivo = f'{nombre_original}_{int(time.time())}{extension}'

        # Guardar la imagen en un directorio específico en el servidor
        with open('/root/documents/' + nombre_archivo, 'wb+') as destino:
            for chunk in imagen.chunks():
                destino.write(chunk)
        
        url_documento = '/root/documents/' + nombre_archivo
        logger.debug(url_documento)
        try:
            logger.debug(body['document_id'])
            documento_requerido =DocumentoRequerido.objects.get(documento_requerido_id=int(body['document_id']))
            curp                =Solicitantes.objects.get(curp=body['curp'])
            ruta_documento      =url_documento
            
        except (TypeError, ValueError):
            # Manejar el caso cuando el valor sea nulo o no se pueda convertir a entero
            logger.info('Parámetro faltante en el cuerpo de la solicitud')
            return JsonResponse({'error': 'Parámetro faltante en el cuerpo de la solicitud'}, status=400)
        #busca al usuario en la base de datos
        registros = Documentos.objects.filter(Q(curp=curp)& Q(documento_requerido=documento_requerido)) 
        if registros.exists():
            logger.info('Registro de documento existente')
            return JsonResponse({'error': 'Registro de documento existente'}, status=400)
        else:
            nuevo_objeto = Documentos(curp=curp, documento_requerido=documento_requerido,ruta_documento=ruta_documento)
            nuevo_objeto.save()
            return JsonResponse({'mensaje': 'Imagen guardada exitosamente.'})
    else:
        return JsonResponse({'error': 'No se envió ninguna imagen o el método de solicitud no es POST.'}, status=400)


@csrf_exempt
def obtener_url_documento(request, nombre_documento):
    try:
        url_documento = f'{settings.MEDIA_URL}{nombre_documento}'
        return JsonResponse({'url_documento': url_documento})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)
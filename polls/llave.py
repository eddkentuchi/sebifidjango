#biblioteca de seguridad
from django.views.decorators.csrf import csrf_exempt
#biblioteca para validar
from django.core.exceptions import ValidationError
#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#biblioteca para convertir la respuesta a json utf-8
import json
#biblioteca para generar el hash
import hashlib
import logging
import random
from django.views import View
#biblioteca para hacer peteciones post
import requests

logger = logging.getLogger(__name__)

#class Vista2(View):
#    def get(self, request):
#        data = {
#            'message': 'Vista 2',
#            'data': ['dato4', 'dato5', 'dato6'],
#        }
#        return JsonResponse(data)

#metodo para obtener el valor de la llave CDMX
@csrf_exempt
def Keycdmx(request):
    if request.method == 'POST':
        logger.info('Esta es la Keycdmx') 
        body = json.loads(request.body.decode('utf-8'))  
        #inf = request.GET.get('code')
        logger.debug(body)
        data = {
                'message': 'Vista 2',
                'data': ['dato4', 'dato5', 'dato6'],
            }
        info = {
                    "grantType": "authorization_code",
                    "code": body['code'],
                    "redirectUri":"http://registros.fondeso.cdmx.gob.mx/validacion",
                    "clientId": "202112281143197289",
                    "clientSecret": "MohT5M8gsU7-tsIUcIsZwc1tUnLsWjiAkuoVd1Pz0F"
                }
        logger.info('Esta es la info') 
        logger.debug(info) 
        response = requests.post('https://llave.cdmx.gob.mx/rest/oauth/token', json=info,
                                        auth=('registro_beneficiarios_fodeso',
                                            'R3G1sTr0%B3N3f1c1Ar1os%fond3S0%pR0%28%12%2021'))
        logger.info('Esta es la respuesta') 
        logger.debug(response) 
        if response.status_code == 200:
            logger.info('Esta el if  del token')
            elToken = response.json()['accessToken'].strip()

            headers = {'accessToken': elToken}
            response = requests.get('https://llave.cdmx.gob.mx/rest/oauth/usuario',
                                    auth=('registro_beneficiarios_fodeso',
                                            'R3G1sTr0%B3N3f1c1Ar1os%fond3S0%pR0%28%12%2021'),
                                    headers=headers)

            tempo = response.json()
            response_data = {
                'cad': response.json(),
                'tkn': True,
            }
            logger.info('Esta es la respuesta') 
            logger.debug(response_data)
            logger.info('Esta es la tempo') 
            logger.debug(tempo)
            return JsonResponse(tempo, status=200)
    else:
        return JsonResponse(data)


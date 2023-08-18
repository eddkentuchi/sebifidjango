#biblioteta para las respuestas tipo json
from django.http import JsonResponse
#biblioteca para las vistas
from django.views import View
#Llamado de modelos para referencias
from .models import Sexo,TipoPoblacion,Etnia,EstadoCivil
from .models import Sectores,TiposCredito,DocumentoRequerido
from .models import NivelesCredito
#Biblioteca para imprimir en terminal
import logging
#biblioteca de tiempo
import time

logger = logging.getLogger(__name__)
#trae todas las etnias
class Etnias(View):
    def get(self, request):
        
        respuestas = Etnia.objects.values('etnia_id','etnia')
        resp_list = [{'id': respuesta['etnia_id'],'datavalue': respuesta['etnia']} for respuesta in respuestas]
        return JsonResponse(list(resp_list), safe=False)
#trae tod0s los estados civiles
class EdoCivils(View):
    def get(self, request):
        
        respuestas = EstadoCivil.objects.values('estado_civil_id','estado_civil')
        resp_list = [{'id': respuesta['estado_civil_id'],'datavalue': respuesta['estado_civil']} for respuesta in respuestas]
        return JsonResponse(list(resp_list), safe=False)
#trae todos los sexos
class Sexos(View):
    def get(self, request):
        
        respuestas = Sexo.objects.values('sexo_id','sexo')
        resp_list = [{'id': respuesta['sexo_id'],'datavalue': respuesta['sexo']} for respuesta in respuestas]
        return JsonResponse(list(resp_list), safe=False)
#trae todos los tipos de poblacion
class TipoPoblacions(View):
    def get(self, request):
        
        respuestas = TipoPoblacion.objects.values('tipo_poblacion_id','tipo_poblacion')
        resp_list = [{'id': respuesta['tipo_poblacion_id'],'datavalue': respuesta['tipo_poblacion']} for respuesta in respuestas]
        return JsonResponse(list(resp_list), safe=False)
#trae toda la información de creditos de tipo micricreditos
class CreditosMicrocreditos(View):
    def get(self, request):
        tipo_credito = 'Financiamiento Microcréditos'
        respuestas = TiposCredito.objects.filter(tipo_credito=tipo_credito).values('tipo_credito_id','codigo','nombre_credito','descripcion_tipo_credito','objetivo','procedimiento_id')
        resultado = []
        for respuesta in respuestas:
                idcredit = respuesta['tipo_credito_id']
                codigo = respuesta['codigo']
                datavalue = respuesta['nombre_credito']
                # Realiza consultas para obtener los niveles más alto y más bajo
                niveles = NivelesCredito.objects.filter(tipo_credito_id=idcredit)

                nivel_alto = niveles.order_by('-nivel').first()
                nivel_bajo = niveles.order_by('nivel').first()
                
                # Si existen niveles, agrega la información al resultado
                if nivel_alto and nivel_bajo:
                    resultado.append({
                        'id': idcredit,
                        'codigo' : codigo,
                        'datavalue': datavalue,
                        'level': float(nivel_alto.nivel),
                        'monto_max': float(nivel_alto.monto_maximo),
                        'monto_min': float(nivel_bajo.monto_minimo),
                        'tasa': float(nivel_bajo.tasa_ordinaria),
                    })
        #logger.debug(resultado)
        
        resultado_ordenado = sorted(resultado, key=lambda x: x['codigo'])
        logger.debug(resultado_ordenado)
        return JsonResponse(list(resultado_ordenado), safe=False)
#trae toda la información de creditos de tipo negocio
class CreditosNegocios(View):
    def get(self, request):
        tipo_credito = 'Financiamiento Negocio'
        respuestas = TiposCredito.objects.filter(tipo_credito=tipo_credito).values('tipo_credito_id','codigo','nombre_credito','descripcion_tipo_credito','objetivo','procedimiento_id')
        resultado = []
        for respuesta in respuestas:
                idcredit = respuesta['tipo_credito_id']
                codigo = respuesta['codigo']
                datavalue = respuesta['nombre_credito']
                # Realiza consultas para obtener los niveles más alto y más bajo
                niveles = NivelesCredito.objects.filter(tipo_credito_id=idcredit)

                nivel_alto = niveles.order_by('-nivel').first()
                nivel_bajo = niveles.order_by('nivel').first()
                
                # Si existen niveles, agrega la información al resultado
                if nivel_alto and nivel_bajo:
                    resultado.append({
                        'id': idcredit,
                        'codigo': codigo,
                        'datavalue': datavalue,
                        'level': float(nivel_alto.nivel),
                        'monto_max': float(nivel_alto.monto_maximo),
                        'monto_min': float(nivel_bajo.monto_minimo),
                        'tasa': float(nivel_bajo.tasa_ordinaria),
                    })
        resultado_ordenado = sorted(resultado, key=lambda x: x['codigo'])
        logger.debug(resultado_ordenado)
        return JsonResponse(list(resultado_ordenado), safe=False)
#trae toda la información de creditos de tipo empresa
class CreditosEmpresas(View):
    def get(self, request):
        tipo_credito = 'Financiamiento Empresa'
        respuestas = TiposCredito.objects.filter(tipo_credito=tipo_credito).values('tipo_credito_id','codigo','nombre_credito','descripcion_tipo_credito','objetivo','procedimiento_id')
        resultado = []
        for respuesta in respuestas:
                idcredit = respuesta['tipo_credito_id']
                codigo = respuesta['codigo']
                datavalue = respuesta['nombre_credito']
                # Realiza consultas para obtener los niveles más alto y más bajo
                niveles = NivelesCredito.objects.filter(tipo_credito_id=idcredit)

                nivel_alto = niveles.order_by('-nivel').first()
                nivel_bajo = niveles.order_by('nivel').first()
                # Si existen niveles, agrega la información al resultado
                if nivel_alto and nivel_bajo:
                    resultado.append({
                        'id': idcredit,
                        'codigo' : codigo,
                        'datavalue': datavalue,
                        'level': float(nivel_alto.nivel),
                        'monto_max': float(nivel_alto.monto_maximo),
                        'monto_min': float(nivel_bajo.monto_minimo),
                        'tasa': float(nivel_bajo.tasa_ordinaria),
                    })
        resultado_ordenado = sorted(resultado, key=lambda x: x['codigo'])
        logger.debug(resultado_ordenado)
        return JsonResponse(list(resultado_ordenado), safe=False)
#trae los giros de negocio segun el factor
class SectoresGiros(View):
    def get(self, request):
        respuestas = Sectores.objects.values('sector_id','sector')
        resp_list = [{'id': respuesta['sector_id'],'datavalue': respuesta['sector']} for respuesta in respuestas]
        return JsonResponse(list(resp_list), safe=False)
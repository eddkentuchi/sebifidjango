from django.urls import path
from . import codigop, llave, vfupone, exportlist,vfdocumentos,logins,validaciones
from . import creagrupos,busquedasavanzadas,creanegocios
from . import views
from . import token
urlpatterns = [
    #paths post
    path('keyCdmx',         llave.Keycdmx,                      name='keyCdmx'),
        
    path('vfupone/',        vfupone.Userdata,                   name='vfuno1'),
    path('vfuponeaddress/', vfupone.Userdataddress,             name='vfuponeaddress'),
    path('creagrupos/',     creagrupos.CrearGrupos,             name='creagrupos'),
    path('crearnegocio/',   creanegocios.CrearNegocios,         name='crearnegocio'),
    
    path('vfdocumentos/',   vfdocumentos.Guardardocumento,      name='vfdocumentos'),
    
    path('login/',          logins.login,                       name='login'),
    path('recuperausuario/',logins.recuperaUsuario,             name='recuperausuario'),
    path('recuperacontra/', logins.recuperaContrase,            name='recuperacontra'),
    path('userwithdir/',    logins.UserWithDir,                 name='userwithdir'),
    path('infodeusuario/',  logins.DatosUsuario,                name='infodeusuario'),
    
    path('validacurp/',     validaciones.ValidaCurp,            name='validacurp'),
    path('validagendocs/',  validaciones.ValidaGenDocs,         name='validagendocs'),
    
    path('busexpcurp/',     busquedasavanzadas.BExpeCurp,       name='busexpcurp'),
    path('busdirecciones/', busquedasavanzadas.BDirecciones,    name='busdirecciones'),
    path('codigopostal/',   busquedasavanzadas.CodigoPostal,    name='codigopostal'),
    path('giros/',          busquedasavanzadas.BuscaGiros,      name='giros'),
    path('creditdocs/',     busquedasavanzadas.CreditDocsList,  name='creditdocs'),
    path('detallescredit/', busquedasavanzadas.DetallesCredit,  name='detallescredit'),
    path('docsgenerales/',  busquedasavanzadas.DocsGenerales,   name='docsgenerales'),    
    #paths get
    path('etnias/',         exportlist.Etnias.as_view(),                name='etnias'),
    path('edocivils/',      exportlist.EdoCivils.as_view(),             name='edocivils'),
    path('sexos/',          exportlist.Sexos.as_view(),                 name='sexos'),
    path('tipopoblacions/', exportlist.TipoPoblacions.as_view(),        name='tipopoblacions'),
    path('credimicros/',    exportlist.CreditosMicrocreditos.as_view(), name='credimicro'),
    path('credinegocios/',  exportlist.CreditosNegocios.as_view(),      name='credinegocios'),   
    path('crediempresas/',  exportlist.CreditosEmpresas.as_view(),      name='crediempresas'),
    
    path('sectoresgiros/',  exportlist.SectoresGiros.as_view(),         name='sectoresgiros'),
    #paths de prueba
    path('get-csrf-token/', token.get_csrf_token,   name='token'),
    path("",                views.polls,            name="polls"),
    #path('set-csrf-cookie/', codigop.set_csrf_cookie, name='set_csrf_cookie'),
    
]


    #response = requests.post(url, headers=headers, json=data)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AsignacionBancos(models.Model):
    credito = models.ForeignKey('Creditos', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del crédito')
    banco = models.ForeignKey('Bancos', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del banco')
    asignacion_bancos_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'asignacion_bancos'


class AsignacionModulo(models.Model):
    credito = models.ForeignKey('Creditos', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del crédito')
    modulo = models.ForeignKey('Modulo', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del módulo')
    asignacion_modulo_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'asignacion_modulo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bancos(models.Model):
    banco_id = models.AutoField(primary_key=True, db_comment='Identificador del banco')
    banco = models.CharField(unique=True, max_length=255, db_comment='Nombre del banco')

    class Meta:
        managed = False
        db_table = 'bancos'


class Carteraold(models.Model):
    expediente = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    primer_apellido = models.CharField(max_length=250, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=250, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=50, blank=True, null=True)
    no_identificacion = models.CharField(max_length=100, blank=True, null=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    no_grupo = models.CharField(max_length=50, blank=True, null=True)
    fecha_operacion = models.CharField(max_length=50, blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    calle = models.CharField(max_length=250, blank=True, null=True)
    colonia = models.CharField(max_length=250, blank=True, null=True)
    codigo_postal = models.CharField(max_length=50, blank=True, null=True)
    alcaldia = models.CharField(max_length=100, blank=True, null=True)
    monto_credito = models.FloatField(blank=True, null=True)
    entrega = models.CharField(max_length=50, blank=True, null=True)
    estatus_credito = models.CharField(max_length=50, blank=True, null=True)
    saldo_credito = models.FloatField(blank=True, null=True)
    tipo_credito = models.CharField(max_length=150, blank=True, null=True)
    nombre_completo = models.CharField(max_length=500, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=50, blank=True, null=True)
    curp = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.CharField(max_length=150, blank=True, null=True)
    saldo_final = models.CharField(max_length=50, blank=True, null=True)
    estatus_fecha = models.CharField(blank=True, null=True)
    estatus_curp = models.CharField(blank=True, null=True)
    fecha_liberacion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carteraold'


class CasosLegales(models.Model):
    legal_id = models.AutoField(primary_key=True, db_comment='Identificador del expediente legal')
    credito = models.ForeignKey('Creditos', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del crédito')
    estado_legal = models.ForeignKey('EstadosLegales', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del estado legal')
    fecha_inicio = models.DateField(db_comment='Fecha del inicio del proceso legal')
    fecha_fin = models.DateField(blank=True, null=True, db_comment='Fecha del termino del proceso legal')
    caso_legal = models.TextField(blank=True, null=True, db_comment='Descripción del caso legal')

    class Meta:
        managed = False
        db_table = 'casos_legales'


class Cobranzas(models.Model):
    cobranza_id = models.AutoField(primary_key=True, db_comment='Identificador de cobranza')
    credito = models.ForeignKey('Creditos', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del crédito')
    tipo_cobranza = models.ForeignKey('TiposCobranza', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del tipo de cobranza')
    fecha_inicio = models.DateField(db_comment='Fecha de inicio de cobranza')
    fecha_fin = models.DateField(blank=True, null=True, db_comment='Fecha de termino de cobranza')
    cobranza = models.TextField(blank=True, null=True, db_comment='Descripción de cobranza')

    class Meta:
        managed = False
        db_table = 'cobranzas'


class Colonias(models.Model):
    colonia_id = models.AutoField(primary_key=True, db_comment='Identificador de colonia')
    colonia = models.CharField(max_length=255, db_comment='Nombre de la colonia')
    codigo_postal = models.CharField(max_length=10, blank=True, null=True, db_comment='Código Postal')
    municipio = models.ForeignKey('Municipios', models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del municipio')
    tipo_asentamiento = models.CharField(max_length=50, blank=True, null=True, db_comment='Tipo de asentamiento')
    es_prioritaria = models.IntegerField(blank=True, null=True, db_comment='Especifica si es colonia prioritaria')

    class Meta:
        managed = False
        db_table = 'colonias'


class Creditos(models.Model):
    credito_id = models.AutoField(primary_key=True, db_comment='Llave primaria del crédito')
    folio = models.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='Folio del crédito individual o grupal')
    tipo_credito_solicitado = models.ForeignKey('TiposCredito', models.DO_NOTHING, blank=True, null=True, db_comment='Llave foranea del tipo de crédito')
    nivel_credito = models.ForeignKey('NivelesCredito', models.DO_NOTHING, blank=True, null=True, db_comment='Llave foranea del nivel de crédito')
    fecha_solicitud = models.DateField(blank=True, null=True, db_comment='Fecha en la que finaliza su solicitud del crédito')
    monto_asignado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto autorizado del crédito')
    tipo_plazo = models.ForeignKey('Periodicidad', models.DO_NOTHING, blank=True, null=True, db_comment='Tipo de plazo mensual, quincenal')
    numero_plazos = models.IntegerField(blank=True, null=True, db_comment='Números de plazos')
    numero_pagos = models.IntegerField(blank=True, null=True, db_comment='Número de pagos')
    numero_periodo_gracia = models.IntegerField(blank=True, null=True, db_comment='Número de periodo de gracia')
    seguro = models.ForeignKey('Seguros', models.DO_NOTHING, blank=True, null=True, db_comment='Llave foranea del seguro contratado')
    tipo_garantia = models.ForeignKey('TiposGarantia', models.DO_NOTHING, blank=True, null=True, db_comment='Llave foranea de tipo de garantia')
    monto_garantia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto de la garantia')
    referencia_bancaria = models.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='Referencia bancaria asignada para el pago en bancos')
    fecha_formalizacion = models.DateField(blank=True, null=True, db_comment='Fecha de formalización')
    fecha_inicial_cobro = models.DateField(blank=True, null=True, db_comment='Fecha inicial en la que se puede ir a cobrar el crédito al banco')
    fecha_final_cobro = models.DateField(blank=True, null=True, db_comment='Fecha máxima en la que se puede ir a cobrar el crédito al banco')
    fecha_primer_pago = models.DateField(blank=True, null=True, db_comment='Fecha del primer pago')
    estatus_general = models.CharField(max_length=50, blank=True, null=True, db_comment='Estatus general del crédito')
    monto_pago = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Importe del pago de 1 a n-1')
    monto_pago_final = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='importe del pago final para obtener un monto cerrado')
    monto_asignado_letra = models.CharField(max_length=255, blank=True, null=True, db_comment='Monto asisgando de crédito escrito en letra para formatos')
    tipo_credito_asignado = models.ForeignKey('TiposCredito', models.DO_NOTHING, related_name='creditos_tipo_credito_asignado_set', blank=True, null=True, db_comment='Es el crédito que FONDESO asisgnó a esta solicitud')
    tipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, blank=True, null=True, db_comment='Es el tipo de persona que solicita el crédito')
    fecha_registro = models.DateField(blank=True, null=True, db_comment='Fecha en la que inicia el proceso de crédito')

    class Meta:
        managed = False
        db_table = 'creditos'


class Cursos(models.Model):
    curso_id = models.BigAutoField(primary_key=True)
    curp = models.ForeignKey('Solicitantes', models.DO_NOTHING, db_column='curp')
    credito = models.ForeignKey(Creditos, models.DO_NOTHING, blank=True, null=True)
    curso_fecha = models.DateField(blank=True, null=True)
    curso_valido = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos'


class Direcciones(models.Model):
    direccion_id = models.AutoField(primary_key=True, db_comment='Identificador de la dirección')
    alias = models.CharField(max_length=50, db_comment='alias de la dirección "Casa" "Oficina"')
    calle = models.CharField(max_length=255, blank=True, null=True, db_comment='Nombre de la calle')
    num_exterior = models.CharField(max_length=10, blank=True, null=True, db_comment='Número exterior')
    num_interior = models.CharField(max_length=10, blank=True, null=True, db_comment='Número interior')
    colonia = models.ForeignKey(Colonias, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador de la colonia')
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True, db_comment='Teléfono fijo del domicilio')
    entre_calles = models.CharField(max_length=500, blank=True, null=True, db_comment='Calles entre las que se encuentra el domicilio')
    referencia_domicilio = models.CharField(max_length=500, blank=True, null=True, db_comment='Datos de referencia para ubicar el domicilio')
    editable = models.IntegerField(blank=True, null=True, db_comment='Indica si es permitida la edición del registro')

    class Meta:
        managed = False
        db_table = 'direcciones'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentoRequerido(models.Model):
    documento_requerido_id = models.AutoField(primary_key=True, db_comment='Identificador del requisito')
    tipo_credito = models.ForeignKey('TiposCredito', models.DO_NOTHING, blank=True, null=True, db_comment='ID del tipo de crédito al que corresponde del requisito')
    tipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, blank=True, null=True, db_comment='ID del tipo de persona al que corresponde del requisito')
    documento_requerido = models.CharField(max_length=150, blank=True, null=True, db_comment='Nombre del requisito')
    documento_requerido_hint = models.CharField(blank=True, null=True, db_comment='Descripción o explicación del requisito')
    documento_requerido_url_formato = models.CharField(blank=True, null=True, db_comment='URL donde se puede obtener el formato y/o instrucciones del requisito')
    documento_requerido_url_ayuda = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento_requerido'


class Documentos(models.Model):
    documento_id = models.AutoField(primary_key=True, db_comment='identificador del documento')
    curp = models.ForeignKey('Solicitantes', models.DO_NOTHING, db_column='curp', blank=True, null=True, db_comment='CURP del solicitante')
    documento_requerido = models.ForeignKey(DocumentoRequerido, models.DO_NOTHING, blank=True, null=True, db_comment='Nombre del tipo de documento')
    ruta_documento = models.CharField(max_length=255, blank=True, null=True, db_comment='Ubicación de la carpeta donde se encuentra el documento')
    activo = models.BooleanField(blank=True, null=True, db_comment='Nombre del archivo del documento')
    uid_documento = models.CharField(max_length=255, blank=True, null=True, db_comment='UID del documento')
    comentarios = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class EstadoCivil(models.Model):
    estado_civil_id = models.IntegerField(primary_key=True)
    estado_civil = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class Estados(models.Model):
    estado_id = models.AutoField(primary_key=True, db_comment='Identificador del estado')
    estado = models.CharField(max_length=255, db_comment='Nombre del estado')
    abreviatura = models.CharField(max_length=10, blank=True, null=True, db_comment='Abreviatura del estado acorde al CURP')
    pais = models.CharField(max_length=10, blank=True, null=True, db_comment='País del estado')

    class Meta:
        managed = False
        db_table = 'estados'


class EstadosLegales(models.Model):
    estado_legal_id = models.AutoField(primary_key=True, db_comment='Identificador del estado legal')
    estado_legal = models.CharField(unique=True, max_length=255, db_comment='Estado legal')

    class Meta:
        managed = False
        db_table = 'estados_legales'


class EstadosProceso(models.Model):
    estado_proceso_id = models.AutoField(primary_key=True, db_comment='Identificador del estado del proceso')
    estado_proceso = models.CharField(unique=True, max_length=255, db_comment='Estado del proceso')

    class Meta:
        managed = False
        db_table = 'estados_proceso'


class Etnia(models.Model):
    etnia_id = models.IntegerField(primary_key=True)
    etnia = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'etnia'


class Expediente(models.Model):
    expediente_id = models.BigAutoField(primary_key=True, db_comment='Identificador autonumerico del expediente se mantiene en nivel 4 y 5 donde el grupo puede separarse')
    expediente = models.CharField(max_length=50, blank=True, null=True, db_comment='Folio del expediente FDSO + ID')
    hash_expediente = models.CharField(max_length=250, blank=True, null=True, db_comment='HASH para encripción de elementos')

    class Meta:
        managed = False
        db_table = 'expediente'


class Extranjero(models.Model):
    curp = models.ForeignKey('Solicitantes', models.DO_NOTHING, db_column='curp', db_comment='CURP de persona extranjera')
    documento_acreditacion = models.CharField(max_length=50, blank=True, null=True, db_comment='Nombre del documento que acredita su estatus migratorio')
    fecha_vencimiento = models.DateField(blank=True, null=True, db_comment='Fecha de vencimiento del documento')
    actividad_autorizada = models.CharField(max_length=50, blank=True, null=True, db_comment='Actividad autorizada')

    class Meta:
        managed = False
        db_table = 'extranjero'


class Folios(models.Model):
    folio = models.OneToOneField('Solicitantes', models.DO_NOTHING, primary_key=True, db_comment='Identificador único y secuencial de los folios generados')
    curp = models.CharField(max_length=18, db_comment='CURP al que fue asignado esta secuencia de folio')
    fecha_registro = models.DateField(db_comment='Fecha en que se realizo la asignación del secuencial y el CURP')

    class Meta:
        managed = False
        db_table = 'folios'


class Giros(models.Model):
    giro_id = models.AutoField(primary_key=True, db_comment='Identificador del giro')
    giro = models.CharField(unique=True, max_length=255, db_comment='Giro del negocio')
    sector = models.ForeignKey('Sectores', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giros'


class Grupo(models.Model):
    grupo_id = models.BigAutoField(primary_key=True, db_comment='Identificador del grupo')
    nombre_grupo = models.CharField(max_length=120, blank=True, null=True, db_comment='Nombre del grupo si es individual es el nombre del titular')
    tipo_grupo = models.ForeignKey('TipoGrupo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class Log(models.Model):
    log_id = models.AutoField(primary_key=True, db_comment='Identificador del LOG')
    fecha = models.DateTimeField(db_comment='Fecha del registro')
    modulo = models.CharField(max_length=50, db_comment='Módulo al que pertenece el registro')
    accion = models.CharField(max_length=50, db_comment='Acción realizada')
    categoria = models.CharField(max_length=50, db_comment='Categoría del mensaje')
    usuario = models.CharField(max_length=255, db_comment='Usuario que realizó la acción')
    ip = models.CharField(max_length=255, db_comment='IP desde la que se realizó la acción')
    comentario = models.TextField(db_comment='Comentario o mensjae de error detallado')

    class Meta:
        managed = False
        db_table = 'log'


class Metadatos(models.Model):
    metadato_id = models.AutoField(primary_key=True, db_comment='identificador del registro de metadatos')
    clave = models.CharField(unique=True, max_length=255, db_comment='Clave única del metadato')
    valor = models.CharField(max_length=255, db_comment='Valor del metadato')
    descripcion = models.TextField(blank=True, null=True, db_comment='Descripción para entender el uso del metadato')

    class Meta:
        managed = False
        db_table = 'metadatos'


class Modulo(models.Model):
    modulo_id = models.AutoField(primary_key=True, db_comment='Identificador del módulo')
    modulo = models.CharField(unique=True, max_length=255, db_comment='Nombre del módulo')
    zona = models.CharField(max_length=255, db_comment='Nombre de la zona a la pertenece el módulo')
    alcaldia = models.CharField(max_length=255, db_comment='Alcaldía a la que pertenece el módulo')
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    horario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class Municipios(models.Model):
    municipio_id = models.AutoField(primary_key=True, db_comment='identificador del municipio')
    municipio = models.CharField(max_length=255, db_comment='Nombre del municipio')
    estado = models.ForeignKey(Estados, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del estado al que pertenece el municipio')

    class Meta:
        managed = False
        db_table = 'municipios'


class Negocio(models.Model):
    negocio_id = models.AutoField(primary_key=True, db_comment='Identificador númerico unico y auto generado del negocio')
    denominacion_razon_social = models.CharField(max_length=255, db_comment='Denominación o razón social')
    rfc = models.CharField(unique=True, max_length=13, db_comment='Registro Federal de Contribuyentes R.F.C del negocio')
    giro = models.ForeignKey(Giros, models.DO_NOTHING, blank=True, null=True, db_comment='Sector productivo al que pertenece el negocio')
    telefono_negocio = models.CharField(max_length=15, blank=True, null=True, db_comment='Télefono del negocio')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='Correo del negocio')
    numero_acta_constitutiva = models.CharField(max_length=50, blank=True, null=True, db_comment='Número o Folio del acta constitutiva')
    fecha_otorgamiento = models.DateField(blank=True, null=True, db_comment='Fecha de otorgamiento del acta constitutiva')
    nombre_quien_expide = models.CharField(max_length=255, blank=True, null=True, db_comment='Nombre del notario, corredor público o alcardía que expide')
    numero_notaria = models.CharField(max_length=50, blank=True, null=True, db_comment='Número de la notaria o correduría')
    entidad_federativa_acta = models.CharField(max_length=50, blank=True, null=True, db_comment='Entidad Federativa donde se expidio el Acta constitutiva o póliza')
    numero_registro_publico = models.CharField(max_length=50, blank=True, null=True, db_comment='Folio ó Número de Inscripción en el Registro Público de la Propiedad y de Comercio')
    fecha_registro_publico = models.DateField(blank=True, null=True, db_comment='Fecha de inscripción en el Registro Público de la Propiedad y de Comercio')
    tipo_poder = models.CharField(max_length=50, blank=True, null=True, db_comment='Tipo de Poder Notarial con el que acredita la representación')
    numero_poder = models.CharField(max_length=50, blank=True, null=True, db_comment='Número o Folio del Instrumento o documento con el que acredita la representación')
    nombre_notario_poder = models.CharField(max_length=255, blank=True, null=True, db_comment='Nombre del Notario Corredor Público o Juez del instrumento o documento con el que acredita la representación')
    numero_notaria_poder = models.CharField(max_length=50, blank=True, null=True, db_comment='Número de Notaría Correduría o Juzgado del instrumento o documento con el que acredita la representación')
    entidad_federativa_poder = models.CharField(max_length=50, blank=True, null=True, db_comment='Entidad Federativa del Instrumento o documento con el que acredita la representación')
    registro_publico_poder = models.CharField(max_length=50, blank=True, null=True, db_comment='Inscripción en el Registro Público de la Propiedad y de Comercio del instrumento o documento con el que acredita la representación')

    class Meta:
        managed = False
        db_table = 'negocio'


class NivelesCredito(models.Model):
    nivel_credito_id = models.AutoField(primary_key=True, db_comment='Llave primaria de niveles de Crédito')
    tipo_credito = models.ForeignKey('TiposCredito', models.DO_NOTHING, blank=True, null=True, db_comment='Llave foranea que Define el Tipo de Crédito al que pertenece')
    nivel = models.IntegerField(db_comment='Número de nivel')
    tipo_plazo = models.ForeignKey('Periodicidad', models.DO_NOTHING, blank=True, null=True, db_comment='Llave del tipo de plazo que puede tener el nivel de crédito')
    numero_plazos = models.IntegerField(blank=True, null=True, db_comment='Número de plazos del nivel de crédito')
    monto_minimo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto mínimo otorgable para el nivel de crédito')
    monto_maximo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto máximo otorgable para el nivel de crédito')
    tasa_ordinaria = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tasa de interes ordinaria del nivel de crédito')
    tasa_moratoria = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Tasa de interes moratorio del nivel de crédito')
    periodo_gracia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveles_credito'


class Pagos(models.Model):
    pago_id = models.AutoField(primary_key=True, db_comment='Identificador del pago')
    fecha_pago = models.DateField(db_comment='Fecha del pago')
    metodo_pago = models.CharField(max_length=255, db_comment='Método de pago')
    referencia_bancaria = models.ForeignKey(Creditos, models.DO_NOTHING, db_column='referencia_bancaria', to_field='referencia_bancaria', blank=True, null=True, db_comment='Referencia bancaria')
    interes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto de los intereses pagados')
    capital = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto del pago a capital')
    seguro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto del pago del seguro')
    pago_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Monto del pago total')
    numero_pago = models.IntegerField(blank=True, null=True, db_comment='Número de pago realizado')

    class Meta:
        managed = False
        db_table = 'pagos'


class ParametrosGenerales(models.Model):
    parametro_general_id = models.IntegerField(db_comment='Identificador del parámetro')
    clave = models.CharField(max_length=50, blank=True, null=True, db_comment='Clave del parámetro')
    valor = models.CharField(max_length=255, blank=True, null=True, db_comment='Valor del parámetro')
    vigencia = models.CharField(max_length=50, blank=True, null=True, db_comment='Vigencia del parametro')
    descripcion = models.TextField(blank=True, null=True, db_comment='Descripción del parámetro')

    class Meta:
        managed = False
        db_table = 'parametros_generales'


class Periodicidad(models.Model):
    tipo_plazo_id = models.AutoField(primary_key=True, db_comment='llave primaria del plazo')
    tipo_plazo = models.CharField(max_length=255, db_comment='Descripción del tipo de plazo Mensual, Quincenal, etc.')

    class Meta:
        managed = False
        db_table = 'periodicidad'


class Procedimientos(models.Model):
    procedimiento_pasos_id = models.AutoField(primary_key=True, db_comment='Identificador del procedimiento')
    procedimiento_paso = models.CharField(max_length=255, db_comment='Nombre del proceso')
    paso_orden = models.IntegerField(blank=True, null=True, db_comment='Orden de los pasos del proceso')
    paso_url = models.CharField(max_length=500, blank=True, null=True, db_comment='URL del procedimiento')
    tipo_credito = models.ForeignKey('TiposCredito', models.DO_NOTHING, blank=True, null=True, db_comment='Procedimiento a mostrar del crédito')

    class Meta:
        managed = False
        db_table = 'procedimientos'


class RegistroProceso(models.Model):
    registro_proceso_id = models.AutoField(primary_key=True, db_comment='Identificador del registro del proceso')
    credito = models.ForeignKey(Creditos, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del crédito')
    estado_proceso = models.ForeignKey(EstadosProceso, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del estado del proceso')
    fecha_cambio_estado = models.DateField(db_comment='Fecha del cambio de estado')
    responsable_id = models.IntegerField(db_comment='Identificador del responsable')

    class Meta:
        managed = False
        db_table = 'registro_proceso'


class RelDireccionCurp(models.Model):
    rel_direccion_curp_id = models.AutoField(primary_key=True, db_comment='Identificador de la relación por compatibilidad por DJANGO')
    curp = models.ForeignKey('Solicitantes', models.DO_NOTHING, db_column='curp', db_comment='CURP')
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_comment='Identificador de la dirección')
    fecha_vigencia = models.DateField(db_comment='Fecha de vigencia')

    class Meta:
        managed = False
        db_table = 'rel_direccion_curp'


class RelDireccionNegocio(models.Model):
    negocio = models.ForeignKey(Negocio, models.DO_NOTHING, db_comment='Identificador del negocio')
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_comment='Identificador de la dirección')
    fecha_vigencia = models.DateField(db_comment='Fecha de vigencia')
    rel_direccion_negocio_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rel_direccion_negocio'


class RelExpedienteCredito(models.Model):
    expediente = models.ForeignKey(Expediente, models.DO_NOTHING, blank=True, null=True)
    credito = models.ForeignKey(Creditos, models.DO_NOTHING, blank=True, null=True)
    sesion = models.ForeignKey('Sesiones', models.DO_NOTHING, blank=True, null=True)
    rel_expediente_credito_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rel_expediente_credito'


class RelExpedienteCurp(models.Model):
    expediente = models.ForeignKey(Expediente, models.DO_NOTHING, blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del grupo')
    curp = models.ForeignKey('Solicitantes', models.DO_NOTHING, db_column='curp', blank=True, null=True, db_comment='CURP de los solicitantes')
    es_obligado_solidario = models.BooleanField(blank=True, null=True, db_comment='Indica si es obligado solidario, en un crédito grupal todos son obligados solidarios')
    es_representante = models.BooleanField(blank=True, null=True, db_comment='Indica si es responsable o titular del grupo o representante legal')
    secuencial = models.IntegerField(blank=True, null=True, db_comment='Registra la secuencia del alta de lis integrantes del grupo')
    negocio = models.ForeignKey(Negocio, models.DO_NOTHING, blank=True, null=True)
    rel_expediente_curp_id = models.BigAutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_expediente_curp'


class Roles(models.Model):
    rol_id = models.AutoField(primary_key=True, db_comment='Identificador del ROL')
    rol = models.CharField(max_length=255, db_comment='Nombre del ROL')

    class Meta:
        managed = False
        db_table = 'roles'


class Sectores(models.Model):
    sector_id = models.AutoField(primary_key=True, db_comment='Identificador del sector')
    sector = models.CharField(unique=True, max_length=255, db_comment='Nombre del sector')

    class Meta:
        managed = False
        db_table = 'sectores'


class Seguros(models.Model):
    seguro_id = models.AutoField(primary_key=True, db_comment='Llave primaria de Seguro contratado')
    costo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_comment='Costo del seguro')
    tipo = models.CharField(max_length=255, blank=True, null=True, db_comment='Tipo de seguro contratado')
    aseguradora = models.CharField(max_length=255, blank=True, null=True, db_comment='Nombre de la aseguradora')
    vigencia = models.DateField(blank=True, null=True, db_comment='Fecha de vigencia de la póliza')
    poliza = models.CharField(max_length=255, blank=True, null=True, db_comment='Número o folio de la póliza')
    numero_renovacion = models.IntegerField(blank=True, null=True, db_comment='Número de renovación actual')
    renovaciones = models.IntegerField(blank=True, null=True, db_comment='Número máximo de renovaciones')
    tipo_renovacion = models.CharField(blank=True, null=True, db_comment='Tipo de renovación anual, semestral')

    class Meta:
        managed = False
        db_table = 'seguros'


class Sesiones(models.Model):
    sesion_id = models.AutoField(primary_key=True, db_comment='Identificador de la sesión')
    sesion = models.CharField(max_length=50, blank=True, null=True, db_comment='Nombre de la sesión')
    fecha_sesion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesiones'


class Sexo(models.Model):
    sexo_id = models.AutoField(primary_key=True)
    sexo = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'sexo'


class Solicitantes(models.Model):
    curp = models.CharField(primary_key=True, max_length=18, db_comment='CURP del solicitante')
    nombre = models.CharField(max_length=255, db_comment='Nombre(s) del solicitante')
    primer_apellido = models.CharField(max_length=255, db_comment='primer apellido del solicitante')
    segundo_apellido = models.CharField(max_length=255, blank=True, null=True, db_comment='Segundo apellido del solicitante')
    telefono = models.CharField(max_length=15, blank=True, null=True, db_comment='Teléfono móvil del solicitante')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='Correo electrónico del solicitante')
    fecha_nacimiento = models.DateField(blank=True, null=True, db_comment='Fecha de nacimiento del solicitante')
    sexo = models.ForeignKey(Sexo, models.DO_NOTHING, blank=True, null=True, db_comment='Sexo del solicitante')
    estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, blank=True, null=True, db_comment='Estado civil del solicitante')
    tipo_poblacion = models.ForeignKey('TipoPoblacion', models.DO_NOTHING, blank=True, null=True, db_comment='Tipo de población del solicitante')
    grupo_vulnerable = models.BooleanField(blank=True, null=True, db_comment='Indica si el solicitante pertenece a un grupo vulnerable')
    grupo_prioritario = models.BooleanField(blank=True, null=True, db_comment='Indica si el solicitante pertenece a un grupo prioritario')
    etnia = models.ForeignKey(Etnia, models.DO_NOTHING, blank=True, null=True, db_comment='Nombre de la étnia a la que pertenece')
    identificacion_oficial = models.CharField(max_length=50, blank=True, null=True, db_comment='Nombre de la identificación oficial')
    numero_identificacion = models.CharField(max_length=50, blank=True, null=True, db_comment='Número de la identificación oficial')
    nacionalidad = models.CharField(max_length=50, blank=True, null=True, db_comment='Nacionalidad')
    hash = models.CharField(max_length=128, blank=True, null=True, db_comment='Hash de la solicitud')
    folio = models.CharField(max_length=15, blank=True, null=True)
    folio_id = models.BigIntegerField(unique=True, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitantes'


class TipoGrupo(models.Model):
    tipo_grupo_id = models.AutoField(primary_key=True)
    tipo_grupo = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_grupo'


class TipoPersona(models.Model):
    tipo_persona_id = models.IntegerField(primary_key=True)
    tipo_persona = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class TipoPoblacion(models.Model):
    tipo_poblacion_id = models.IntegerField(primary_key=True)
    tipo_poblacion = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_poblacion'


class TiposCobranza(models.Model):
    tipo_cobranza_id = models.AutoField(primary_key=True, db_comment='Identificador de cobranza')
    tipo_cobranza = models.CharField(unique=True, max_length=255, db_comment='Nombre de la cobranza')

    class Meta:
        managed = False
        db_table = 'tipos_cobranza'


class TiposCredito(models.Model):
    tipo_credito_id = models.AutoField(primary_key=True, db_comment='Llave del tipo de crédito')
    codigo = models.CharField(unique=True, max_length=4, db_comment='Código de referencia del crédito')
    nombre_credito = models.CharField(max_length=255, db_comment='Nombre del crédito')
    descripcion_tipo_credito = models.CharField(blank=True, null=True, db_comment='Descripción a mostrar del crédito')
    objetivo = models.CharField(blank=True, null=True, db_comment='Objetivo a mostrar del crédito')
    procedimiento_id = models.IntegerField(blank=True, null=True, db_comment='Procedimiento a mostrar del crédito')
    tipo_credito = models.CharField(max_length=50, blank=True, null=True)
    tipo_credito_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_credito'


class TiposGarantia(models.Model):
    tipo_garantia_id = models.AutoField(primary_key=True, db_comment='Identificador de la garantia')
    garantia = models.CharField(max_length=255, blank=True, null=True, db_comment='Descripción de la garantia')

    class Meta:
        managed = False
        db_table = 'tipos_garantia'


class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True, db_comment='Identificador del usuario')
    nombre_usuario = models.CharField(unique=True, max_length=255, db_comment='Nombre el usuario')
    contrasena = models.CharField(max_length=255, db_comment='Contraseña del usuario')
    rol = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True, db_comment='Identificador del ROL')
    email = models.CharField(max_length=255, blank=True, null=True, db_comment='Correo electrónico del usuario')
    activo = models.BooleanField(blank=True, null=True, db_comment='Indica si el usuario esta activo')

    class Meta:
        managed = False
        db_table = 'usuarios'

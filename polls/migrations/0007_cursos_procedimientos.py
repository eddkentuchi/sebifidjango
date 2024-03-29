# Generated by Django 4.2.2 on 2023-08-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_documentorequerido_tipopersona_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('curso_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('curso_fecha', models.DateField(blank=True, null=True)),
                ('curso_valido', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Procedimientos',
            fields=[
                ('procedimiento_pasos_id', models.AutoField(db_comment='Identificador del procedimiento', primary_key=True, serialize=False)),
                ('procedimiento_paso', models.CharField(db_comment='Nombre del proceso', max_length=255)),
                ('paso_orden', models.IntegerField(blank=True, db_comment='Orden de los pasos del proceso', null=True)),
                ('paso_url', models.CharField(blank=True, db_comment='URL del procedimiento', max_length=500, null=True)),
            ],
            options={
                'db_table': 'procedimientos',
                'managed': False,
            },
        ),
    ]

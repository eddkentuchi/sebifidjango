# Generated by Django 4.2.2 on 2023-06-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tblestado',
            fields=[
                ('idestado', models.IntegerField(db_column='IdEstado', primary_key=True, serialize=False)),
                ('nombreestado', models.CharField(blank=True, db_column='NombreEstado', max_length=50, null=True)),
                ('nombreabreviado', models.CharField(blank=True, db_column='NombreAbreviado', max_length=30, null=True)),
            ],
            options={
                'db_table': 'tblestado',
                'managed': False,
            },
        ),
    ]

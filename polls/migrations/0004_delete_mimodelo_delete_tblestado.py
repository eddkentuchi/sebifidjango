# Generated by Django 4.2.2 on 2023-06-22 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_campo2_mimodelo_estado_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MiModelo',
        ),
        migrations.DeleteModel(
            name='Tblestado',
        ),
    ]

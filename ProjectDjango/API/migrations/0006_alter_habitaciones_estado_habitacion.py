# Generated by Django 3.2.9 on 2021-11-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20211123_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitaciones',
            name='Estado_habitacion',
            field=models.CharField(choices=[('1', 'Disponible'), ('2', 'No Disponible')], max_length=2),
        ),
    ]

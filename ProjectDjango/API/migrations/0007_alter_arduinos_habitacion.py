# Generated by Django 3.2.9 on 2021-11-23 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_alter_habitaciones_estado_habitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arduinos',
            name='Habitacion',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='habitacion_arduinos', to='API.habitaciones'),
        ),
    ]

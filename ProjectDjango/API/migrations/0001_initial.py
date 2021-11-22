# Generated by Django 3.2.9 on 2021-11-22 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=15)),
                ('Correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='habitaciones')),
                ('Estado_habitacion', models.CharField(max_length=1)),
                ('Cerradura_electronica', models.BooleanField(default=True)),
                ('Wifi', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_habitacion', models.CharField(max_length=100)),
                ('Cantidad_camas', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_inicio', models.DateField()),
                ('Fecha_fin', models.DateField()),
                ('Precio_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Token', models.CharField(max_length=100)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.cliente')),
                ('Habitaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.habitaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Hoteles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_hotel', models.CharField(max_length=100)),
                ('Ubicacion', models.CharField(max_length=100)),
                ('Calificacion', models.DecimalField(decimal_places=0, max_digits=1)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='hoteles')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_hoteles', to='API.categorias')),
            ],
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='Hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_habitaciones', to='API.hoteles'),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='Tipo_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_habitacion_habitaciones', to='API.hoteles'),
        ),
        migrations.CreateModel(
            name='Arduinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arduino', models.CharField(max_length=100)),
                ('Temperatura', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Estado_ventalidor', models.BooleanField(default=True)),
                ('Estado_calefactor', models.BooleanField(default=True)),
                ('Habitaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.habitaciones')),
            ],
        ),
    ]
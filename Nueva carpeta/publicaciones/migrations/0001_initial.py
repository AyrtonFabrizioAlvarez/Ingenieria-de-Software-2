# Generated by Django 5.0.4 on 2024-05-03 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listados', '0001_initial'),
        ('sesiones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('aceptada', models.BooleanField()),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listados.categoria')),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesiones.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=160)),
                ('fecha', models.DateTimeField()),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesiones.usuario')),
                ('publicacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion')),
            ],
        ),
    ]

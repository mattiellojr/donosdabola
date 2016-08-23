# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
                ('descricao', models.TextField()),
                ('horario_disponivel_de', models.TimeField(default=django.utils.timezone.now)),
                ('horario_disponivel_ate', models.TimeField(default=django.utils.timezone.now)),
                ('valor_hora', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('cpf_cnpj', models.CharField(max_length=15)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_reserva', models.DateField(default=django.utils.timezone.now)),
                ('reservado_de', models.TimeField(default=django.utils.timezone.now)),
                ('reservado_ate', models.TimeField(default=django.utils.timezone.now)),
                ('campo', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='core.Campo')),
                ('reservado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
    ]

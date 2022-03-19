# Generated by Django 3.2.12 on 2022-03-17 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('sex', models.BooleanField()),
            ],
            options={
                'verbose_name': 'farmer',
                'verbose_name_plural': 'farmers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Propertie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('size', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=10000, max_length=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=10000, max_length=22)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='api_v1.farmer')),
            ],
            options={
                'verbose_name': 'propertie',
                'verbose_name_plural': 'properties',
                'ordering': ['id'],
                'unique_together': {('id', 'farmer')},
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('sex', models.BooleanField()),
                ('breed', models.CharField(max_length=255)),
                ('code', models.DecimalField(decimal_places=1, max_digits=100)),
                ('furr_color', models.CharField(max_length=100)),
                ('purchased', models.BooleanField()),
                ('birth_date', models.DateField()),
                ('propertie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='api_v1.propertie')),
            ],
            options={
                'verbose_name': 'animal',
                'verbose_name_plural': 'animals',
                'ordering': ['id'],
                'unique_together': {('id', 'propertie')},
            },
        ),
        migrations.CreateModel(
            name='Milking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('shift', models.CharField(max_length=100)),
                ('dry', models.BooleanField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milkings', to='api_v1.animal')),
            ],
            options={
                'verbose_name': 'milking',
                'verbose_name_plural': 'milkings',
                'ordering': ['id'],
                'unique_together': {('id', 'animal')},
            },
        ),
    ]

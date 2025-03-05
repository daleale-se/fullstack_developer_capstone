# Generated by Django 5.1.6 on 2025-02-28 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[ ('id', models.BigAutoField(auto_created=True,
                                                primary_key=True,
                                                serialize=False,
                                                verbose_name='ID')),
                ('dealer_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'),
                                                   ('SUV', 'SUV'),
                                                   ('Wagon', 'Wagon'),
                                                   ('Coupe', 'Coupe'),
                                                   ('Convertible',
                                                    'Convertible'),
                                                   ('Hatchback',
                                                    'Hatchback'),
                                                   ('Pickup', 'Pickup')],
                                          default='Sedan', max_length=20)),
                ('year', models.DateField()),
                ('price', models.DecimalField(blank=True, decimal_places=2,
                                              max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_make', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='models', to='djangoapp.carmake')),
            ],
        ),
    ]

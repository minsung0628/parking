# Generated by Django 4.0.2 on 2022-06-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingLot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(blank=True, max_length=10, null=True)),
                ('handicap', models.CharField(blank=True, max_length=2, null=True)),
                ('enter', models.DateField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'parking',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsModel', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='seat',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='yearOfModel',
            field=models.DateField(blank=True),
        ),
    ]
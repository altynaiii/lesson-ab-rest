# Generated by Django 3.2.7 on 2023-01-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]

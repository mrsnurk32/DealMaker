# Generated by Django 2.0.7 on 2018-08-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='date',
            field=models.DateField(default='2018-08-22'),
        ),
    ]

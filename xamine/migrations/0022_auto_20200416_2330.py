# Generated by Django 3.0.5 on 2020-04-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0021_auto_20200416_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
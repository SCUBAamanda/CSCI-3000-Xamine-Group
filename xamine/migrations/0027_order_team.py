# Generated by Django 3.0.5 on 2020-04-18 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0026_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='xamine.Team'),
        ),
    ]

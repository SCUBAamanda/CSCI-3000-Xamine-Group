# Generated by Django 3.0.5 on 2020-04-21 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0028_auto_20200419_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='xamine.Order'),
        ),
    ]
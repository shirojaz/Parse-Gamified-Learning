# Generated by Django 5.0 on 2023-12-10 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='menus.category'),
        ),
    ]

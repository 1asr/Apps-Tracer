# Generated by Django 5.1.2 on 2024-10-18 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_status_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.status'),
        ),
    ]
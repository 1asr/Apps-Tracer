# Generated by Django 5.1.2 on 2024-10-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_projects_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='techstack',
        ),
        migrations.AddField(
            model_name='projects',
            name='techstack',
            field=models.ManyToManyField(to='app1.technology'),
        ),
    ]
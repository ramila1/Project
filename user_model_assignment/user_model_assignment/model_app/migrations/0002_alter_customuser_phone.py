# Generated by Django 5.0.5 on 2024-05-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(max_length=10, null=True, unique=True),
        ),
    ]
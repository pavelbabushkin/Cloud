# Generated by Django 5.0.7 on 2024-08-03 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='pasword',
            new_name='password',
        ),
    ]

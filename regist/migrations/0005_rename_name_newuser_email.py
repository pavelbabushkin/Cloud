# Generated by Django 5.0.7 on 2024-08-04 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0004_delete_usergames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='name',
            new_name='email',
        ),
    ]

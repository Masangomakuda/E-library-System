# Generated by Django 3.2.9 on 2021-11-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auth_user',
            new_name='User',
        ),
    ]
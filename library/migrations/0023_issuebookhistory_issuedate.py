# Generated by Django 4.0.1 on 2022-03-17 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_rename_book_issuebookhistory_booksid'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebookhistory',
            name='issuedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 4.0.1 on 2022-03-15 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_rename_bookid_issuebookhistory_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebookhistory',
            old_name='book',
            new_name='booksid',
        ),
    ]

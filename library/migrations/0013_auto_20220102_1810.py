# Generated by Django 3.2.9 on 2022-01-02 16:10

import datetime
from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_issuedbooks_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['lastname']},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='books',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issuedbooks',
            name='due_date',
            field=models.DateTimeField(default=library.models.get_due_date),
        ),
        migrations.AlterField(
            model_name='issuedbooks',
            name='issuedate',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
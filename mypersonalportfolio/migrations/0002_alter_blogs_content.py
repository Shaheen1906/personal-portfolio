# Generated by Django 5.2.2 on 2025-06-07 20:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypersonalportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 4.1 on 2022-09-14 11:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_imageabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='mini_text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

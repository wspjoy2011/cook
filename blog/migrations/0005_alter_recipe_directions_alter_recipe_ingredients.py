# Generated by Django 4.1 on 2022-08-18 15:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

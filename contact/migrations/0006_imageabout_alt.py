# Generated by Django 4.1 on 2022-09-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageabout',
            name='alt',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

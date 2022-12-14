# Generated by Django 4.1 on 2022-09-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_about_mini_text_alter_about_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='users_icons_socials/%Y/%m/%d/')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]

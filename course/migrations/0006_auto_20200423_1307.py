# Generated by Django 3.0.5 on 2020-04-23 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200423_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='user',
            new_name='author',
        ),
    ]

# Generated by Django 3.2.5 on 2022-02-21 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='valut',
            new_name='value',
        ),
    ]

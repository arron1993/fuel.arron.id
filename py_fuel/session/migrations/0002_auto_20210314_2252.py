# Generated by Django 3.1.7 on 2021-03-14 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lap',
            old_name='session',
            new_name='session_id',
        ),
    ]

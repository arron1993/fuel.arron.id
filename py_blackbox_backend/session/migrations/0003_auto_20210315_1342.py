# Generated by Django 3.1.7 on 2021-03-15 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_auto_20210314_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='lap',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lap',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='session',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

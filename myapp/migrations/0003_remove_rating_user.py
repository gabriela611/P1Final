# Generated by Django 5.2 on 2025-04-25 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_service_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]

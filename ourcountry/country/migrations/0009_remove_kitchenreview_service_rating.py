# Generated by Django 5.1.4 on 2025-01-09 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0008_remove_favorite_country_favorite_alter_favorite_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchenreview',
            name='service_rating',
        ),
    ]

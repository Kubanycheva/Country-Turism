# Generated by Django 5.1.4 on 2025-03-11 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0054_rename_created_date_attractionreview_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractionreview',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='hotelsreview',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='kitchenreview',
            old_name='created_at',
            new_name='created_date',
        ),
    ]

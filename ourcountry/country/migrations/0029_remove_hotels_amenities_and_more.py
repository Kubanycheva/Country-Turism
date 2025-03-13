# Generated by Django 5.1.4 on 2025-03-07 11:40

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0028_alter_attractionreview_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='safety_and_hygiene',
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=55)),
                ('amenity_en', models.CharField(max_length=55, null=True)),
                ('amenity_ru', models.CharField(max_length=55, null=True)),
                ('amenity_ar', models.CharField(max_length=55, null=True)),
                ('icon', models.FileField(upload_to='icons/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='country.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='CultureKitchenMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='culture_kitchen_image')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='culture_kitchen_image')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='culture_kitchen_image')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='culture_kitchen_image')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='SafetyAndHygiene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('name_en', models.CharField(max_length=55, null=True)),
                ('name_ru', models.CharField(max_length=55, null=True)),
                ('name_ar', models.CharField(max_length=55, null=True)),
                ('icon', models.FileField(upload_to='icons/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safety_and_hygiene', to='country.hotels')),
            ],
        ),
    ]

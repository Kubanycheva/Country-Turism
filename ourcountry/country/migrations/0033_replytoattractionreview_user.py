# Generated by Django 5.1.4 on 2025-03-07 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0032_replytoattractionreview_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='replytoattractionreview',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

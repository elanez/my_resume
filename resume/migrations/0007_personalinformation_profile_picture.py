# Generated by Django 5.1.6 on 2025-04-08 06:42

import resume.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=resume.models.profile_picture_upload_path),
        ),
    ]

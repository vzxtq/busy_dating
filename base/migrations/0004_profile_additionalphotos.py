# Generated by Django 5.1.4 on 2025-01-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_additionalphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='additionalPhotos',
            field=models.ImageField(blank=True, null=True, upload_to='additional_photos/'),
        ),
    ]

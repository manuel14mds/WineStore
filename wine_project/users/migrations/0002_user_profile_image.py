# Generated by Django 3.2.5 on 2022-08-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image/'),
        ),
    ]

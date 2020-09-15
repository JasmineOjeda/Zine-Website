# Generated by Django 3.1 on 2020-09-11 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0002_socialmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='cover',
        ),
        migrations.AddField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(default='staff/profile_pic/default.jpg', upload_to='staff/profile_pic/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='related_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

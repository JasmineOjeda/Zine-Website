# Generated by Django 3.1 on 2020-09-11 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0006_auto_20200911_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='staff',
            name='related_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]

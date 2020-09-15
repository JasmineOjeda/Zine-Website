# Generated by Django 3.1 on 2020-09-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20200908_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='cover',
            field=models.ImageField(null=True, upload_to='magazine/static/magazine/covers/'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='headline',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]

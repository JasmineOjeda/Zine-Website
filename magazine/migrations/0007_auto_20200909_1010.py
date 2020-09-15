# Generated by Django 3.1 on 2020-09-09 17:10

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20200908_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='cover',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/static/'), upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='magazine_file',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/static/'), upload_to='pdf_files'),
        ),
    ]
# Generated by Django 3.1 on 2020-09-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0013_auto_20200909_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='cover',
            field=models.ImageField(null=True, upload_to='magazine/covers'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='magazine_file',
            field=models.FileField(null=True, upload_to=']magazine/pdf_files'),
        ),
    ]
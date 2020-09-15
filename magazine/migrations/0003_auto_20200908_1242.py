# Generated by Django 3.1 on 2020-09-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20200904_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='date_published',
        ),
        migrations.AddField(
            model_name='magazine',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='cover',
            field=models.ImageField(upload_to='magazine/static/magazine/covers/'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='magazine_file',
            field=models.FileField(null=True, upload_to='magazine/static/magazine/pdf_files/'),
        ),
    ]

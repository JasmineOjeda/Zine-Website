# Generated by Django 3.1 on 2020-09-09 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0002_auto_20200909_1406'),
        ('article', '0005_auto_20200908_1250'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stream_Highlight',
            new_name='StreamHighlight',
        ),
    ]
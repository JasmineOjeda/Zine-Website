# Generated by Django 3.1 on 2020-09-14 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0017_auto_20200914_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='related_magazine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.magazine'),
        ),
    ]
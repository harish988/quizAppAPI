# Generated by Django 2.2.10 on 2020-05-15 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'managed': True, 'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelTable(
            name='rating',
            table='rating',
        ),
    ]
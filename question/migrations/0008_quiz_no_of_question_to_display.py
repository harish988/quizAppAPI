# Generated by Django 2.2.10 on 2020-05-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20200515_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='no_of_question_to_display',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
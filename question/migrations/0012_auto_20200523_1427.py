# Generated by Django 3.0.3 on 2020-05-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_auto_20200523_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(null=True, upload_to='quiz/staticfiles'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(null=True, upload_to='quiz/staticfiles'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_image',
            field=models.ImageField(null=True, upload_to='quiz/staticfiles'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-05-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20200514_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domain',
            options={'managed': True, 'verbose_name_plural': 'Domains'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'managed': True, 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz_type',
            field=models.CharField(choices=[('SINGLECHOICE', 'SingleChoice'), ('MULTIPLECHOICE', 'MultipleChoice'), ('TEXT', 'Text')], max_length=20),
        ),
        migrations.AlterModelTable(
            name='domain',
            table='domain',
        ),
        migrations.AlterModelTable(
            name='quiz',
            table='quiz',
        ),
    ]
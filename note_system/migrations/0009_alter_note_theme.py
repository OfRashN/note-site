# Generated by Django 3.2 on 2021-07-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_system', '0008_alter_note_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='theme',
            field=models.CharField(default='Без названия', max_length=40),
        ),
    ]

# Generated by Django 3.2 on 2021-07-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_system', '0003_alter_note_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='is_public',
            field=models.BooleanField(),
        ),
    ]

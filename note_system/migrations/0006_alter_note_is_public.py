# Generated by Django 3.2 on 2021-07-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_system', '0005_alter_note_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='is_public',
            field=models.BooleanField(),
        ),
    ]

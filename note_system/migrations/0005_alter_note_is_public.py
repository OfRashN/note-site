# Generated by Django 3.2 on 2021-07-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_system', '0004_alter_note_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
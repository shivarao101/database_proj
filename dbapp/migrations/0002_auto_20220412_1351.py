# Generated by Django 3.0.8 on 2022-04-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='college',
        ),
    ]
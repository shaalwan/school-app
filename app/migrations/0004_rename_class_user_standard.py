# Generated by Django 3.2.7 on 2021-09-29 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_roll_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Class',
            new_name='standard',
        ),
    ]
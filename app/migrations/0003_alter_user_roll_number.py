# Generated by Django 3.2.7 on 2021-09-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roll_number',
            field=models.IntegerField(default=0),
        ),
    ]
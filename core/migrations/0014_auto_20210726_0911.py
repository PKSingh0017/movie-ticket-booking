# Generated by Django 3.2.5 on 2021-07-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210725_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipes',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
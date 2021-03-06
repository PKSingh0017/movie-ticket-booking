# Generated by Django 3.2.5 on 2021-12-05 14:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_movie_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='pk', editable=False, populate_from='name', unique=True),
            preserve_default=False,
        ),
    ]

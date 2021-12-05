# Generated by Django 3.2.5 on 2021-07-15 07:04

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('core', '0006_alter_testimonial_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ingredients',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

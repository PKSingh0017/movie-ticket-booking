# Generated by Django 3.2.5 on 2021-07-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_blog_contactmessage_newsletter_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestributionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipes',
            options={'verbose_name_plural': 'Recipes'},
        ),
    ]

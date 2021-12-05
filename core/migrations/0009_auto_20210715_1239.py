# Generated by Django 3.2.5 on 2021-07-15 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210715_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='key_ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
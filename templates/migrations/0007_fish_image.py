# Generated by Django 2.2.2 on 2019-10-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0006_fish'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

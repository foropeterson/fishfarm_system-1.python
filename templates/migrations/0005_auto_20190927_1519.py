# Generated by Django 2.2.2 on 2019-09-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0004_auto_20190926_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fmsapp.Department'),
        ),
    ]

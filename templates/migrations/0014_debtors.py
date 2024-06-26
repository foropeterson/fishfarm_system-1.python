# Generated by Django 2.2.2 on 2019-10-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0013_sales_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('file_no', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('signature', models.ImageField(upload_to='')),
            ],
        ),
    ]

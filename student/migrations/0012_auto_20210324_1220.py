# Generated by Django 3.1.5 on 2021-03-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_admission_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cources',
            name='Book_lang',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='specific_crc',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

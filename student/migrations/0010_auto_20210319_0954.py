# Generated by Django 3.1.5 on 2021-03-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210319_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cources',
            name='Book_desc',
            field=models.CharField(max_length=1000),
        ),
    ]

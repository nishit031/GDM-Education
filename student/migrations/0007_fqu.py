# Generated by Django 3.1.5 on 2021-03-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20210316_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fqu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Que', models.CharField(max_length=100)),
                ('Ans', models.CharField(max_length=2000)),
            ],
        ),
    ]

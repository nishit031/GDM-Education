# Generated by Django 3.1.5 on 2021-03-12 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FstName', models.CharField(max_length=20)),
                ('LstName', models.CharField(max_length=20)),
                ('Subject', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=25)),
                ('CPassword', models.CharField(max_length=25)),
                ('TNC', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Comment', models.CharField(max_length=200)),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FstName', models.CharField(max_length=20)),
                ('MidName', models.CharField(max_length=20)),
                ('LstName', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('Country', models.CharField(choices=[('India', 'India'), ('Canada', 'Canada'), ('USA', 'USA'), ('Austria', 'Austria'), ('Bangladesh', 'Bangladesh'), ('Iran', 'Iran'), ('Japan', 'Japan'), ('China', 'China')], max_length=30)),
                ('Phone', models.PositiveIntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('Line', models.TextField(max_length=100)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Code', models.PositiveIntegerField()),
                ('AdharCard', models.ImageField(upload_to='images/')),
                ('Passport', models.ImageField(upload_to='images/')),
                ('Fmarksheet', models.ImageField(upload_to='images/')),
                ('Smarksheet', models.ImageField(upload_to='images/')),
                ('Signature', models.ImageField(upload_to='images/')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.registration')),
            ],
        ),
    ]

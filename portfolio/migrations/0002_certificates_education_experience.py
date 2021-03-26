# Generated by Django 3.1.7 on 2021-03-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='certificates/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('educational_institution', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_beginning', models.IntegerField()),
                ('end_date', models.IntegerField()),
                ('place_of_work', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]

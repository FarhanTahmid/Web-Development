# Generated by Django 4.0.5 on 2022-08-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0010_remove_courseregistrations_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complains',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Bull Name')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact No')),
                ('email', models.CharField(max_length=30, verbose_name='E mail')),
                ('facebookid', models.CharField(max_length=100, verbose_name='Facebook ID')),
                ('instaid', models.CharField(max_length=100, verbose_name='Instagram ID')),
                ('linkedinid', models.CharField(max_length=100, verbose_name='Linkedin ID')),
                ('snapid', models.CharField(max_length=100, verbose_name='Snapchat ID')),
                ('prove', models.ImageField(upload_to='proves')),
            ],
        ),
    ]
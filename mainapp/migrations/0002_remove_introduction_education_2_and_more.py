# Generated by Django 4.0.2 on 2022-02-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introduction',
            name='Education_2',
        ),
        migrations.RemoveField(
            model_name='introduction',
            name='Institution_Name2',
        ),
        migrations.RemoveField(
            model_name='introduction',
            name='Time2',
        ),
        migrations.AlterField(
            model_name='introduction',
            name='Time',
            field=models.CharField(max_length=100),
        ),
    ]

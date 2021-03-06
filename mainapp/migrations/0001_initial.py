# Generated by Django 4.0.2 on 2022-02-07 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edu_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experince_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exp_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=11, verbose_name=' Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('About', models.TextField(blank=True, null=True)),
                ('Institution_Name', models.CharField(max_length=100)),
                ('Time', models.DateField()),
                ('Institution_Name2', models.CharField(max_length=100)),
                ('Time2', models.DateField()),
                ('skill_1', models.CharField(max_length=100, verbose_name='Skill...')),
                ('skill_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill...')),
                ('skill_3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill...')),
                ('skill_4', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill...')),
                ('skill_5', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skill...')),
                ('Experience_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Experinece')),
                ('Organization_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organization /Company')),
                ('Experience_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Experinece')),
                ('Organization_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organization /Company')),
                ('Language_Proficiency', models.CharField(max_length=100)),
                ('Education_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.edu_level')),
                ('Education_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mainapp.edu_level')),
                ('Experince_Name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.experince_type')),
                ('Experince_Name2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mainapp.experince_type')),
            ],
        ),
    ]

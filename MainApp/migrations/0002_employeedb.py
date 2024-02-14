# Generated by Django 4.2.6 on 2023-10-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(blank=True, max_length=50, null=True)),
                ('eage', models.CharField(blank=True, max_length=50, null=True)),
                ('egender', models.CharField(blank=True, max_length=50, null=True)),
                ('edepartment', models.CharField(blank=True, max_length=50, null=True)),
                ('ediscription', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsaap', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('enumber', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
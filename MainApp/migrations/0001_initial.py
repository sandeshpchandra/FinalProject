# Generated by Django 4.2.4 on 2023-10-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departmentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(blank=True, max_length=50, null=True)),
                ('dhead', models.CharField(blank=True, max_length=50, null=True)),
                ('dtime', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2024-02-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0012_ratedb_userinterestdb_usernotificationdb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremployeedb',
            name='eusername',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

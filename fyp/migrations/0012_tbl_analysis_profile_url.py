# Generated by Django 3.0.3 on 2020-03-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0011_auto_20200301_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_analysis',
            name='profile_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

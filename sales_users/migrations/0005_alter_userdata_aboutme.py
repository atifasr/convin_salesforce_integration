# Generated by Django 3.2.7 on 2021-09-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_users', '0004_auto_20210910_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='aboutme',
            field=models.TextField(blank=True, default='good', null=True),
        ),
    ]

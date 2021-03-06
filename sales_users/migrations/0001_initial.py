# Generated by Django 3.2.7 on 2021-09-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('photourl', models.URLField(null=True)),
                ('billingaddress', models.CharField(max_length=30, null=True)),
                ('account_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.IntegerField(null=True)),
                ('accountid', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('firstname', models.CharField(max_length=40, null=True)),
                ('name', models.CharField(max_length=34, null=True)),
                ('mailingstreet', models.CharField(max_length=30, null=True)),
                ('phone_no', models.CharField(max_length=30, null=True)),
                ('birth_day', models.DateTimeField(null=True)),
                ('lead_source', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('department', models.CharField(max_length=30, null=True)),
                ('photourl', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('company_name', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('timezonesidekey', models.CharField(max_length=20, null=True)),
                ('aboutme', models.TextField(blank=True, default='good')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('isactive', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0021_userrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=256)),
            ],
        ),
    ]

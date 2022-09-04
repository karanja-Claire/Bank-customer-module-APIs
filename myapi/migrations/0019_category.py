# Generated by Django 4.1 on 2022-09-04 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0018_settlement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=256, unique=True)),
                ('category_description', models.CharField(max_length=2000)),
                ('tax_compliance_required', models.BooleanField()),
                ('certificate_of_incorporation_required', models.BooleanField()),
                ('kra_pin', models.BooleanField()),
                ('id_picture_required', models.BooleanField()),
                ('passport_photo', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]

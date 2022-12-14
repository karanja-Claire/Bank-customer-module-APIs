# Generated by Django 4.1 on 2022-09-04 11:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0013_alter_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('mode', models.CharField(choices=[('M-Pesa', 'M-Pesa'), ('Card', 'Card'), ('Wallet', 'Wallet')], max_length=256, null=True)),
                ('source', models.CharField(choices=[('Web', 'Web'), ('USSD', 'USSD'), ('M-Pesa Paybill', 'M-Pesa Paybill')], max_length=256, null=True)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Failed', 'Failed')], max_length=256, null=True)),
                ('transaction_reference', models.CharField(max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapi.bank_account')),
            ],
        ),
    ]

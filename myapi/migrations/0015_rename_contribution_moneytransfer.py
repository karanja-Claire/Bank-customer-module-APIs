# Generated by Django 4.1 on 2022-09-04 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0014_contribution'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contribution',
            new_name='MoneyTransfer',
        ),
    ]
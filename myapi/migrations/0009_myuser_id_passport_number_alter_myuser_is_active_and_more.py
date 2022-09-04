# Generated by Django 4.1 on 2022-09-04 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_rename_bank_name_bank_branch_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='id_passport_number',
            field=models.CharField(default=0, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(blank=True, default=0, null=True)),
                ('approval_status', models.CharField(choices=[('Verified', 'Verified'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('account_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapi.bank_account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapi.myuser')),
            ],
        ),
    ]
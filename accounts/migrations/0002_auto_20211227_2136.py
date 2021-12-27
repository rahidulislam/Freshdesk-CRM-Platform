# Generated by Django 3.2.9 on 2021-12-27 15:36

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('bank_account_name', models.CharField(max_length=25, verbose_name='Bank Account Name')),
                ('bank_account_number', models.IntegerField(unique=True, verbose_name='Bank Account Number')),
                ('account_type', models.CharField(choices=[('savings account', 'Savings Account'), ('current account', 'Current Account'), ('fixed Deposit account', 'Fixed Deposit Account'), ('recurring Deposit account', 'Recurring Deposit Account')], max_length=225, verbose_name='Bank Account Type')),
                ('bank_name', models.CharField(max_length=25, verbose_name='Bank Name')),
                ('bank_short_name', models.CharField(blank=True, max_length=5, null=True, verbose_name='Bank Short Name')),
                ('bank_branch', models.CharField(max_length=25, verbose_name='Bank Branch')),
            ],
            options={
                'verbose_name': 'Bank Account',
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
        migrations.RemoveField(
            model_name='account',
            name='account_description',
        ),
        migrations.RemoveField(
            model_name='account',
            name='account_phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='bank_branch',
        ),
        migrations.RemoveField(
            model_name='account',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name_of_account',
        ),
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+880', max_length=128, region='BD', verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

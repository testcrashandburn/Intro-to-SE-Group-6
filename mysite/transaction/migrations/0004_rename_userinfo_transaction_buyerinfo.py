# Generated by Django 5.0.3 on 2024-03-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_transaction_productinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='userInfo',
            new_name='buyerInfo',
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-30 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('transaction', '0002_transaction_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='productInfo',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
    ]
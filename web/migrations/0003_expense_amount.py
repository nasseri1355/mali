# Generated by Django 5.0.1 on 2024-01-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
    ]

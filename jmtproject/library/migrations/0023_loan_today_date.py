# Generated by Django 3.1.1 on 2020-10-15 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_remove_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='today_date',
            field=models.DateField(default=datetime.date(2020, 10, 15)),
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-15 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_delete_userloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

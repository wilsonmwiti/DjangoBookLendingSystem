# Generated by Django 3.1.1 on 2020-10-15 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_userloan_userlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLoan',
        ),
    ]

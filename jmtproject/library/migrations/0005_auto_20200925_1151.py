# Generated by Django 3.1 on 2020-09-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200924_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]

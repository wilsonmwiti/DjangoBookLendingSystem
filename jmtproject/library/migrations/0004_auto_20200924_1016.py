# Generated by Django 3.1.1 on 2020-09-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200924_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20201007_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='library.Category'),
        ),
    ]

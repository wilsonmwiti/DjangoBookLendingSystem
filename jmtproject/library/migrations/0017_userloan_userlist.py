# Generated by Django 3.1.1 on 2020-10-15 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0016_auto_20201015_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='userloan',
            name='userList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

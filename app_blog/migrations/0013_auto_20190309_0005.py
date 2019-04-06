# Generated by Django 2.1.5 on 2019-03-08 18:35

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0012_auto_20190309_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2019, 3, 8, 18, 35, 39, 234829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

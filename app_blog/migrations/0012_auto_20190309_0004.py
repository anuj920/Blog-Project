# Generated by Django 2.1.5 on 2019-03-08 18:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0011_auto_20190308_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2019, 3, 8, 18, 34, 57, 360497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2019, 3, 8, 18, 34, 57, 359500, tzinfo=utc)),
        ),
    ]

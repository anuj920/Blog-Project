# Generated by Django 2.1.5 on 2019-03-06 20:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0007_auto_20190306_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2019, 3, 6, 20, 27, 18, 589123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.TimeField(default=datetime.datetime(2019, 3, 6, 20, 27, 18, 589123, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.1.5 on 2019-03-11 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0015_auto_20190310_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 2.1.5 on 2019-03-08 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0013_auto_20190309_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

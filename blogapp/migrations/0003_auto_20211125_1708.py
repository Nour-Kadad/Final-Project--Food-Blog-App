# Generated by Django 3.2 on 2021-11-25 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20211125_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 444964)),
        ),
        migrations.AlterField(
            model_name='blogs_comments',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 445961)),
        ),
        migrations.AlterField(
            model_name='get_in_touch',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 448954)),
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 448954)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 447956)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 17, 8, 42, 446959)),
        ),
    ]

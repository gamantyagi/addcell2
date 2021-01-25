# Generated by Django 3.0.2 on 2020-01-31 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0004_auto_20200131_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 648109, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 662616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_participants',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 660504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 662210, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 647592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 661569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 661006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 8, 54, 56, 658799, tzinfo=utc)),
        ),
    ]

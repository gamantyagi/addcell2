# Generated by Django 3.0.2 on 2020-02-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0027_events_event_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_detail',
            field=models.CharField(default='<font size="12px" color="RED">detail of this event is not given</font>', max_length=2000),
        ),
    ]

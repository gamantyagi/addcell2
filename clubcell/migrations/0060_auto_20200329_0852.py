# Generated by Django 3.0.2 on 2020-03-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0059_auto_20200329_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_thumbnail',
            field=models.ImageField(default='event.jpg', upload_to='events/thumbnail'),
        ),
        migrations.AddField(
            model_name='events',
            name='related_images',
            field=models.CharField(default='[]', max_length=1500),
        ),
    ]

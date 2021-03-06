# Generated by Django 3.0.2 on 2020-03-29 18:44

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0060_auto_20200329_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='related_images',
        ),
        migrations.AlterField(
            model_name='events',
            name='event_thumbnail',
            field=versatileimagefield.fields.VersatileImageField(default='event.jpg', upload_to='events/thumbnail'),
        ),
        migrations.CreateModel(
            name='related_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', versatileimagefield.fields.VersatileImageField(default='event.jpg', upload_to='events/related_images')),
                ('alt', models.CharField(default='', max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_images', to='clubcell.events')),
            ],
        ),
    ]

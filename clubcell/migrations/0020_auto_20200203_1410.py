# Generated by Django 3.0.2 on 2020-02-03 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0019_auto_20200203_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='clubcell.clubcell'),
        ),
    ]
# Generated by Django 3.0.2 on 2020-02-03 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubcell', '0015_auto_20200203_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerts',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messages',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL),
        ),
    ]

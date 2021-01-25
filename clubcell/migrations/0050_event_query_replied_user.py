# Generated by Django 3.0.2 on 2020-03-15 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubcell', '0049_auto_20200315_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_query',
            name='replied_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_replied_query', to=settings.AUTH_USER_MODEL),
        ),
    ]
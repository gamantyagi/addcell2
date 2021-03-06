# Generated by Django 3.0.2 on 2020-04-02 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0065_events_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post_commented',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='clubcell.posts'),
        ),
        migrations.AlterField(
            model_name='custom_input',
            name='input_type',
            field=models.CharField(choices=[('T', 'Text'), ('I', 'Integer'), ('C', 'Choice'), ('EMAIL', 'email'), ('MC', 'Multiple Choice')], default='T', max_length=20),
        ),
        migrations.AlterField(
            model_name='like',
            name='post_liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='clubcell.posts'),
        ),
    ]

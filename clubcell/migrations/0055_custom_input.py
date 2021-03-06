# Generated by Django 3.0.2 on 2020-03-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcell', '0054_auto_20200327_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='custom_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_name', models.CharField(max_length=50)),
                ('input_reference', models.CharField(max_length=200)),
                ('input_type', models.CharField(choices=[('T', 'Text'), ('I', 'Integer'), ('C', 'Choice'), ('MC', 'Multiple Choice')], default='T', max_length=3)),
                ('max_length', models.IntegerField(default=50)),
                ('choice_option', models.CharField(blank=True, default=None, max_length=2000, null=True)),
            ],
        ),
    ]

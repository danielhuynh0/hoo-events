# Generated by Django 4.2.6 on 2023-10-19 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoo_event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_time_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_time_start',
        ),
    ]

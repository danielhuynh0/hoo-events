# Generated by Django 4.2.6 on 2023-11-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoo_event', '0008_event_event_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_full_capacity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_capacity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
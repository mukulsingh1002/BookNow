# Generated by Django 4.1.7 on 2023-03-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_event_date_remove_event_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

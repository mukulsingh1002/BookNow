# Generated by Django 4.1.7 on 2023-03-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_meeting1_end_time_remove_meeting1_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting1',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

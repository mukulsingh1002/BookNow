# Generated by Django 4.1.7 on 2023-03-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_event1_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField(default=None)),
                ('start_time', models.TimeField(default=None)),
                ('end_time', models.TimeField(default=None)),
            ],
        ),
    ]

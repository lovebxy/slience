# Generated by Django 2.2.1 on 2020-07-16 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20200716_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='uid',
        ),
    ]

# Generated by Django 2.2.1 on 2020-06-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='content',
            field=models.TextField(blank=True, verbose_name='内容'),
        ),
    ]

# Generated by Django 2.2.1 on 2020-06-14 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('File', '0002_auto_20200614_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'verbose_name': '上级下发文件内容', 'verbose_name_plural': '上级下发文件内容'},
        ),
        migrations.AlterModelTable(
            name='show',
            table='Show',
        ),
    ]
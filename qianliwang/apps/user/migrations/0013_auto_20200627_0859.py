# Generated by Django 2.2.1 on 2020-06-27 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200621_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'verbose_name': '通知/通告/公示', 'verbose_name_plural': '通知/通告/公示'},
        ),
        migrations.AddField(
            model_name='duty',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]

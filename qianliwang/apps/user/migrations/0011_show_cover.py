# Generated by Django 2.2.1 on 2020-06-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200619_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='cover',
            field=models.ImageField(default='icon/default.jpg', upload_to='icon'),
        ),
    ]

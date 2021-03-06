# Generated by Django 2.2.1 on 2020-06-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200611_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='headimg',
            field=models.ImageField(default='icon/default.jpg', upload_to='icon'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, null=True)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('msg', models.ForeignKey(null=True, on_delete=True, to='user.User')),
            ],
        ),
    ]

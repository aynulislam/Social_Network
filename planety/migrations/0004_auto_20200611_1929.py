# Generated by Django 3.0.6 on 2020-06-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planety', '0003_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]

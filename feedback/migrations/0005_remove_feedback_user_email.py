# Generated by Django 2.0.1 on 2018-01-25 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20180125_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user_email',
        ),
    ]
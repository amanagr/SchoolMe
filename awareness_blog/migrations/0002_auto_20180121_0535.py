# Generated by Django 2.0.1 on 2018-01-21 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awareness_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_html',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='teaser_html',
            new_name='teaser',
        ),
    ]
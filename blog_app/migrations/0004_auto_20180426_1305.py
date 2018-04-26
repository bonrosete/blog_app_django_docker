# Generated by Django 2.0.4 on 2018-04-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_blog_category_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_information',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user_information',
            name='lastLogin',
            field=models.DateTimeField(default='1990-01-01 12:00:00'),
            preserve_default=False,
        ),
    ]
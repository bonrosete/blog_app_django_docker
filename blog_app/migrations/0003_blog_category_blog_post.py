# Generated by Django 2.0.4 on 2018-04-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=255)),
                ('categoryDescription', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blogTitle', models.CharField(max_length=255)),
                ('blogMessage', models.TextField()),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('blogCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog_Category')),
                ('blogOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.User_Information')),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class User_Information(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)

class User_Account(models.Model):
    user_id = models.ForeignKey(User_Information, on_delete=models.CASCADE)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

class Blog_Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255)
    categoryDescription = models.CharField(max_length=255)

class Blog_Post(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blogTitle = models.CharField(max_length=255)
    blogMessage = models.TextField()
    blogCategory = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
    blogOwner = models.ForeignKey(User_Information, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now=True)
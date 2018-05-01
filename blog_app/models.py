from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.blogTitle

# class User_Information(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     firstName = models.CharField(max_length=45)
#     lastName = models.CharField(max_length=45)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=1)
#     dateCreated = models.DateTimeField(auto_now=True)
#     lastLogin = models.DateTimeField()

#     def __str__(self):
#         return self.firstName

# class User_Account(models.Model):
#     user_id = models.ForeignKey(User_Information, on_delete=models.CASCADE)
#     username = models.CharField(max_length=45)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

# class Blog_Category(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     categoryName = models.CharField(max_length=255)
#     categoryDescription = models.CharField(max_length=255)

#     def __str__(self):
#         return self.categoryName

# class Blog_Post(models.Model):
#     blog_id = models.AutoField(primary_key=True)
#     blogTitle = models.CharField(max_length=255)
#     blogMessage = models.TextField()
#     blogCategory = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
#     blogOwner = models.ForeignKey(User_Information, on_delete=models.CASCADE)
#     dateCreated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.blogTitle
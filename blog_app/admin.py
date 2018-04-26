from django.contrib import admin
from . models import User_Account, User_Information, Blog_Category, Blog_Post

# Register your models here.

admin.site.register(User_Account)
admin.site.register(User_Information)
admin.site.register(Blog_Category)
admin.site.register(Blog_Post)


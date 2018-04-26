from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import User_Account, User_Information, Blog_Category, Blog_Post
# Create your views here.

# def index(request):
#     return HttpResponse("Hello world!")

def index(request):
    latest_blog_post = Blog_Post.objects.order_by('-dateCreated')[:5]
    context = {
        'latest_blog_post': latest_blog_post,
    }
    return render(request, 'blog_app/index.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog_Post, pk=blog_id)
    return render(request, 'blog_app/detail.html', {'blog': blog})
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import User_Account, User_Information, Blog_Category, Blog_Post
from . forms import LoginForm, SignupForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import datetime

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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if User_Account.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password']).exists():
                return HttpResponseRedirect('/blog/dashboard/')
            else:
                error = "Invalid username or password"
                return render(request, 'blog_app/login.html', {'form':form, 'error':error})
    else:
        form = LoginForm()
    return render(request, 'blog_app/login.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['check_password']:
                
                # Create and save an SQL query that will save the data from the form fields
                createUserInformation = User_Information(firstName=form.cleaned_data['first_name'],
                    lastName=form.cleaned_data['last_name'],
                    age=form.cleaned_data['age'],
                    gender=form.cleaned_data['gender'],
                    lastLogin=datetime.date.today())
                createUserInformation.save()

                # Create and save an SQL query that will save the data from the form fields
                createUserAccount = User_Account(username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    user_id_id=createUserInformation.user_id)
                createUserAccount.save()

                messages.success(request, 'Account created succesfully')
                return HttpResponseRedirect('/blog/signup/')
            else:
                # error = "Password does not match"
                messages.error(request, 'Passwords do not match')
                return render(request, 'blog_app/signup.html', {'form':form})
    else:
        form = SignupForm()
        
    return render(request, 'blog_app/signup.html', {'form':form})

def dashboard(request):
    return render(request, 'blog_app/dashboard.html')
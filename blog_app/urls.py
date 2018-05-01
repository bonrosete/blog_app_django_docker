from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('dashboard/', views.dashboard, name='dashboard'),
]
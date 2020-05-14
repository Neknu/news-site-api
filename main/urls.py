from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'main'
# Be careful setting the name to just /login use userlogin instead!

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.user_login, name='user_login'),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify'),
]
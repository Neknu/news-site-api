from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list_view, name="post_list_view"),
    path('detail/<slug:the_slug>/', views.post_detail_view, name='post_detail_view'),
    path('new/', views.post_new, name="post_new"),
]

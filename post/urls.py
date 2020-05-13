from django.urls import path
from . import views

urlpatterns = [
    path('posts/<slug:the_slug>/', views.post_detail_view, name='show_post'),
]

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('post/', include('post.urls', namespace="post")),
    path('', include('main.urls', namespace="main")),
]

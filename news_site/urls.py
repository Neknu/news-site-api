from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from main.views import verify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('post/', include('post.urls', namespace="post")),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
]

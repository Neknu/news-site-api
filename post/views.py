from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'your_blog/list_post.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'your_blog/show_post.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'


post_detail_view = PostDetailView.as_view()

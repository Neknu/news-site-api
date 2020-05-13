from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'post/list_post.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/show_post.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_view', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/new_post.html', {'form': form})


post_list_view = PostListView.as_view()
post_detail_view = PostDetailView.as_view()

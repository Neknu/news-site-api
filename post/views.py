from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print(request.user)
            post.save()
            print(post.slug)
            return HttpResponseRedirect(
                reverse('post:post_detail_view', args=[post.slug])
            )
    else:
        form = PostForm()
    return render(request, 'post/new_post.html', {'form': form})


post_list_view = login_required(PostListView.as_view())
post_detail_view = login_required(PostDetailView.as_view())

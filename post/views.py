from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'post/list_post.html'

    def get_queryset(self):
        queryset = Post.objects.filter(~Q(status=1))  # On review

        return queryset


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
            if request.user.groups.filter(name__in=['moderator', 'admin']).exists():
                post.status = 2  # Approved
                post.save()
                return HttpResponseRedirect(
                    reverse('post:post_detail_view', args=[post.slug])
                )
            post.save()
            return HttpResponseRedirect(
                reverse('post:post_user')
            )
    else:
        form = PostForm()
    return render(request, 'post/new_post.html', {'form': form})


def post_user(request):
    return render(request, 'post/user_post.html')


post_list_view = login_required(PostListView.as_view())
post_detail_view = login_required(PostDetailView.as_view())

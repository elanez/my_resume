from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def all_posts(request):
    latest_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        "all_posts": latest_posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": post,
        "tags": post.tags.all()
    })

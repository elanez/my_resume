from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.

def all_posts(request):
    latest_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        "all_posts": latest_posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    read_later_list = request.session.get('read_later', [])
    is_in_read_later = slug in read_later_list
    return render(request, 'blog/post-detail.html', {
        "post": post,
        "tags": post.tags.all(),
        "is_in_read_later": is_in_read_later
    })

def read_later_view(request):
    read_later_list = request.session.get('read_later', [])
    posts = Post.objects.filter(slug__in=read_later_list)
    return render(request, 'blog/read-later.html', {
        'posts': posts
    })

def add_to_read_later(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        read_later_list = request.session.get('read_later', [])
        if slug not in read_later_list:
            read_later_list.append(slug)
            request.session['read_later'] = read_later_list
    return redirect('post-detail-page', slug=slug)

def remove_from_read_later(request, slug):
    if request.method == 'POST':
        read_later_list = request.session.get('read_later', [])
        if slug in read_later_list:
            read_later_list.remove(slug)
            request.session['read_later'] = read_later_list
    return redirect('post-detail-page', slug=slug)

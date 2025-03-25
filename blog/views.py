from django.shortcuts import render

# Create your views here.

def all_posts(request):
    return render(request, 'blog/all-posts.html')

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# the . before models means from current directory

def post_list(request):
    #takes a request and returns a function render that will put together our template.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
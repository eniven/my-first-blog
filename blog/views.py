from django.shortcuts import render

def post_list(request):
    #takes a request and returns a function render that will put together our template.
    return render(request, 'blog/post_list.html', {})
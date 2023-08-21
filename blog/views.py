from django.shortcuts import render

# Create your views here.

def blog_index(request):
    return render(request,'blog/blog.html')

def blog_detail(request):
    return render(request,'blog/post-details.html')
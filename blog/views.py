from django.shortcuts import render,get_object_or_404,redirect
from blog.models import post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentsForm
from django.contrib import messages



# Create your views here.

def blog_index(request,**kwargs):
    posts = post.objects.filter(published_date__lte=timezone.now(),status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)


def blog_detail(request,pk):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.SUCCESS, "your comment submitted successfully")
        else:
            messages.add_message(request, messages.ERROR, "your comment didn't submitted")
    
    posts = get_object_or_404(post,pk=pk,status = 1)
    posts.count_views+=1
    posts.save()
    try:
        next = posts.get_next_by_created_date()
    except posts.DoesNotExist:
        next = None
    try:
        previous = posts.get_previous_by_created_date()
    except posts.DoesNotExist:
        previous = None
    if not posts.login_requier:
        comments = Comment.objects.filter(post=posts.id,approved=True).order_by('-created_date')
        form = CommentsForm()
        context = {'posts':posts,'next':next,'previous':previous,'comments':comments,'form':form}
        return render(request,'blog/post-details.html',context)
    #else:
    #    return redirect('/account/login')

def blog_category(request,cat_name):
    posts = post.objects.filter(status=1,category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def blog_search(request):
    posts = post.objects.filter(published_date__lte=timezone.now(),status = 1)
    if request.method=='GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)
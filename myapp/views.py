from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
import datetime
from .forms import PostForm

# Create your views here.

def hello(request, number=6):
    text="<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)


def viewArticle(request, month, year):
   display ="Article no.s is month {0} & year {1}".format(month,year)
   return HttpResponse(display)


def hello(request):
   yooyoo = datetime.datetime.now().date()
   dataset="babaji masti main aag lgegi basti main"
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "myapp/hello.html", {"today" : yooyoo,"data" : dataset,"days_of_week" : daysOfWeek})


def post_list(request):
    posts=Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date') #descending order of publish_Date
    return render(request,"myapp/post_list.html",{'posts': posts})

def post_details(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,"myapp/post_details.html",{'post': post})


def post_new(request):

    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.publish_date=timezone.now()
            post.save()
            return redirect('post_details' , pk=post.pk)

    else :
        form=PostForm()

    return render(request,"myapp/post_edit.html",{'form':form})


def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)

    if request.method=='POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.publish_date=timezone.now()
            post.save()

            return redirect('post_details', pk=post.pk)

    else :
      form = PostForm(instance=post)

    return render(request,"myapp/post_edit.html",{'form':form})
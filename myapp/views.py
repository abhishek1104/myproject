from django.shortcuts import render
from django.http import HttpResponse

import datetime

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
    return render(request,"myapp/post_list.html",{})
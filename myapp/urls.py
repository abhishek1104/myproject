from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [


    url(r'^article/(\d{2})/(\d{4})', views.viewArticle, name='viewArticle'),
    url(r'^hello/' , views.hello , name='hello'),
]
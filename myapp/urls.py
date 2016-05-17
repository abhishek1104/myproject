from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [


    url(r'^article/(\d{2})/(\d{4})', views.viewArticle, name='viewArticle'),
    url(r'^hello/' , views.hello , name='hello'),
    url(r'^$', views.post_list , name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_details, name='post_details'),
    url(r'^post/new/$',views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/', views.post_edit , name='post_edit')
]
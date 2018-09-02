from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]

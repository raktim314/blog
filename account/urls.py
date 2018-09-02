from django.conf.urls import url
from account import views as account_views


urlpatterns = [
    url(r'^signup/$', account_views.signup, name='signup')
]
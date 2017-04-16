from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url


urlpatterns = [
    # /login/
    url(r'^$', views.home, name='home'),
]
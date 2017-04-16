from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url
from details.views import DetailsList
from details.views import DetailsId


urlpatterns = [
    # /login/
#    url(r'^$', views.details, name='details'),
#    url(r'^(?P<album_id>[0-9]+)/$',views.detailsId, name='detailsId'),
    url(r'^$', DetailsList.as_view(), name='details'),
    url(r'^(?P<album_id>[0-9]+)/$', DetailsId.as_view(), name='detailsId'),
]
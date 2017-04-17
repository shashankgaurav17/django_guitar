from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url
from details.views import DetailsList
from details.views import DetailsId
from details.views import BrowseList


urlpatterns = [
    # /login/
#    url(r'^$', views.details, name='details'),
#    url(r'^(?P<album_id>[0-9]+)/$',views.detailsId, name='detailsId'),
    
    url(r'^(?P<album_id>[0-9]+)/$', DetailsId.as_view(), name='detailsId'),
    #browse
    url(r'^browse/$', BrowseList.as_view(), name='browse'),
    #details
    url(r'^details/$', DetailsList.as_view(), name='details'),
    #home
    url(r'^home/$', DetailsList.as_view(), name='home'),
    #login
    url(r'^login/$', DetailsList.as_view(), name='login'),
]
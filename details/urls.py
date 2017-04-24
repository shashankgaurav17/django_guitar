from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url
from details.views import DetailsList
from details.views import DetailsId
from details.views import LoginList


urlpatterns = [
    # /login/
#    url(r'^$', views.details, name='details'),
#    url(r'^(?P<album_id>[0-9]+)/$',views.detailsId, name='detailsId'),
    
    url(r'^details/$', DetailsList.as_view(), name='details'),
    url(r'^details/(?P<album_id>[0-9]+)*', DetailsId.as_view(), name='detailsId'),
    
    #url(r'^details/', DetailsId.as_view(), name='detailsId'),
    #browse
    url(r'^browse/$', views.browse, name='browse'),
    #details
    
    #login
    url(r'^login/$', LoginList.as_view(), name='login'),
    #home
    url(r'', views.home, name='home'),
]
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'guitar1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^password_reset$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('details.urls')),
    
   # url(r'^home/', include('details.urls')),
   # url(r'^browse/', include('details.urls')),
   # url(r'^details/', include('details.urls')),
]

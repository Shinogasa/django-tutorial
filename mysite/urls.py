from django.conf.urls import include, url
from django.contrib import admin

from polls.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^$', index, name='index'),
]

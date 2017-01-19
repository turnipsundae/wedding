from django.conf.urls import url

from . import views

app_name = 'wedding'

urlpatterns = [
    # e.g. /wedding
    url(r'^$', views.index, name='index'),
    # e.g. /wedding/rsvp
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
    url(r'^registry/$', views.registry, name='registry'),
    url(r'^accomodations/$', views.accomodations, name='accomodations'),
    url(r'^test/$', views.test, name='test'),
           
]

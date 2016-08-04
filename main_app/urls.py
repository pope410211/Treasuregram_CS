from django.conf.urls import url
from . import views


#map of urls
urlpatterns = [
    url(r'^$', views.index)
]

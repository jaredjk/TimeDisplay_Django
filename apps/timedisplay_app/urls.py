from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^(?P[0-9]{4})/(?P[0-9]{2}$', views.yourMethodFromUrls)
]
from django.conf.urls import patterns, url

from app1 import views


urlpatterns = patterns(
    '',
    url(r'^page1$', views.page1),
)

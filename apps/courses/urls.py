from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^destroy/(?P<id>[0-9]+)$', views.destroy, name="destroy"),
    url(r'^destroy_really/(?P<id>[0-9]+)$', views.destroy_really, name="destroy_really")
]
from django.conf.urls import include, url
from firstblog import views

urlpatterns = [
    url(r'^$', views.home, name='home')
]
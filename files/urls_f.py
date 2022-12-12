from django.conf.urls import url
from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index),
    url(r'^.*/$', views.index)
]
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    path('',views.index),
    path('<int:movie_id>/', views.movie_detail),
]

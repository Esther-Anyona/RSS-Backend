from django.urls import re_path
from . import views

 
urlpatterns = [ 
    re_path(r'^api/tutorials$', views.favorite),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published)
]
from django.urls import re_path
from . import views

 
urlpatterns = [ 
    re_path(r'^api/recipes/create$', views.create_recipe),
    re_path(r'^api/recipes/(?P<pk>[0-9]+)$', views.get_recipe),
    re_path(r'^api/recipes/search$', views.search_recipes),
    re_path(r'^api/recipes/update$', views.update_recipe),
]
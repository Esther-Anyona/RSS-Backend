from django.urls import re_path, path
from . import views

urlpatterns = [
    path('api/recipes', views.index),
    path('api/recipes/create', views.create_recipe),
    re_path(r'^api/recipes/(?P<pk>[0-9]+)$', views.get_recipe),
    re_path(r'^api/recipes/delete/(?P<pk>[0-9]+)$', views.delete_recipe),
    path('api/recipes/search', views.search_recipes),
    re_path('api/recipes/update/(?P<pk>[0-9]+)$', views.update_recipe),
]
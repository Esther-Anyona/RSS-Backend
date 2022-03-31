from django.urls import re_path, path
from . import views

urlpatterns = [ 
    path('api/recipes/create', views.create_recipe),
    re_path(r'^api/recipes/(?P<pk>[0-9]+)$', views.get_recipe),
    path('api/recipes/search', views.search_recipes),
    path('api/recipes/update', views.update_recipe),
]
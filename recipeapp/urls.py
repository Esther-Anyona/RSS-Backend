from django.urls import re_path, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ratings', views.RatingViewSet, basename='ratings')

urlpatterns = [
    path('api/recipes', views.recipe_list),
    re_path(r'^api/recipes/(?P<pk>[0-9]+)$', views.recipe_detail),
    path('api/recipes/search', views.search_recipes),
    re_path(r'^api/recipes/(?P<pk>[0-9]+)/ratings/$', views.RatingViewSet.as_view({'get': 'list', 'post': 'create'}),name='recipe_ratings'),
]
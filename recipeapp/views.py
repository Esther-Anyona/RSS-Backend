from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Recipe, Rating
from .serializers import RecipeSerializers, RatingSerializers


@api_view(['POST'])
def search(request):
    pass
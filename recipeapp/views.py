from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Recipe, Rating
from .serializers import RecipeSerializer, RatingSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    # view single recipe
    try: 
        recipe = Recipe.objects.get(pk=pk) 
    except Recipe.DoesNotExist: 
        return Response({'message': 'The Recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)
    
    elif request.method == 'PUT':
        recipe_serializer = RecipeSerializer(recipe, request.data)
        if recipe_serializer.is_valid(): 
            recipe_serializer.save() 
            return Response(recipe_serializer.data) 
        return Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        recipe.delete() 
        return Response({'message': 'Recipe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def recipe_list(request):
    # retrieve all recipes
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return Response(recipes_serializer.data)
    
    # create and save new recipe 
    elif request.method == 'POST':
        recipes_serializer = RecipeSerializer(data=request.data)
        if recipes_serializer.is_valid():
            recipes_serializer.save()
            return Response(recipes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(recipes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        count = Recipe.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_recipes(request):
    # retrieve objects by title
    if request.method == 'GET':
        recipes = Recipe.objects.all()

        recipe_name = request.GET.get('recipe_name', None)
        if recipe_name is not None:
            recipes = recipes.filter(recipe_name__icontains=recipe_name)

        recipes_serializer = RecipeSerializer(recipes, many=True)
        return Response(recipes_serializer.data)

class RatingViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all().filter(recipe=self.kwargs['pk'])
        return queryset
    
    # A user can only rate a recipe once
    def create(self, request, *args, **kwargs):
        rating = Rating.objects.filter(recipe=self.kwargs['pk']).first()
        if rating and request.user == rating.rated_by:
            raise PermissionDenied(
                "You can not rate recipe more than once")
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(rated_by=self.request.user)

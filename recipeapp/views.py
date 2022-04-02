from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Rating
from .serializers import RecipeSerializer, RatingSerializer


@api_view(['GET'])
def index(request):
    # retrieve all recipes
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return Response(recipes_serializer.data)


@api_view(['POST'])
def create_recipe(request):
    # create and save new recipe 
    if request.method == 'POST':
        serializers = RecipeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_recipes(request):
    # retrieve objects by title
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        
        recipe_name = request.GET.get('recipe_name', None)
        if recipe_name is not None:
            recipes = recipes.filter(title__icontains=recipe_name)
        
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return Response(recipes_serializer.data, safe=False)


@api_view(['GET'])
def get_recipe(request, pk):
    # view single recipe
    try: 
        recipe = Recipe.objects.get(pk=pk) 
    except Recipe.DoesNotExist: 
        return Response({'message': 'The Recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)


@api_view(['PUT'])
def update_recipe(request, pk):
    # retrieve single recipe
    try: 
        recipe = Recipe.objects.get(pk=pk) 
    except Recipe.DoesNotExist: 
        return Response({'message': 'The Recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        recipe_data = request.data #research
        recipe_serializer = RecipeSerializer(recipe, data=recipe_data) 
        
        if recipe_serializer.is_valid(): 
            recipe_serializer.save() 
            return Response(recipe_serializer.data) 
        return Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_recipe(request, pk):
    # delete single recipe
    try: 
        recipe = Recipe.objects.get(pk=pk) 
    except Recipe.DoesNotExist: 
        return Response({'message': 'The Recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'DELETE': 
        recipe.delete() 
        return Response({'message': 'Recipe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
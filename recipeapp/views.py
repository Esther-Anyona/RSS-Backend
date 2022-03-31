from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Rating
from .serializers import RecipeSerializer, RatingSerializer

@api_view(['POST'])
def create_recipe(request):
    # create and save new recipe 
    if request.method == 'POST':
        recipe = Recipe()
        recipe.recipe_name = request.data['recipe_name']
        recipe.ingredient = request.data['ingredient']
        recipe.category = request.data['category']
        recipe.recipe_pic = request.data['recipe_pic']
        recipe.country = request.data['country']
        recipe.procedure = request.data['procedure']
        recipe.guests_served = request.data['guests_served']
        recipe.created_date = request.data['created_date']
        recipe.save()

        return Response(recipe.data,status=status.HTTP_201_CREATED)


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
    # retrieve single recipe
    try: 
        recipe = Recipe.objects.get(pk=pk) 
    except Recipe.DoesNotExist: 
        return Response({'message': 'The Recipe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)
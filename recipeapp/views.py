from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
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
        recipes_serializer = RecipeSerializer(data=request.data)
        if recipes_serializer.is_valid():
            recipes_serializer.save()
            return Response(recipes_serializer.data, status=status.HTTP_201_CREATED)
        return Response(recipes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        recipe_serializer = RecipeSerializer(recipe, request.data)
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

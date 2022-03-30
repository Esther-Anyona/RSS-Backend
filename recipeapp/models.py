from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images',null=True)
    bio = models.CharField(max_length=120)
    
    def __str__(self):
         return str(self.user)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=120)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    category = models.CharField(max_length=120)
    recipe_pic = models.ImageField(upload_to="images")
    country = models.CharField(max_length=50)
    procedure = models.TextField('Instructions')
    served_guests = models.CharField(max_length=50)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication_date = models.DateTimeField('Date Published')


    def __str__(self):
        return self.recipe_name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

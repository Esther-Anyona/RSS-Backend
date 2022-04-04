from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
    email = models.EmailField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.CharField(max_length=120)

    def __str__(self):
         return str(self.user)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Rating(models.Model):
    choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
        )
    user_rating = models.PositiveBigIntegerField(choices=choices, default=0)
    status = models.CharField(max_length=10, blank=True)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredient = models.TextField()
    category = models.CharField(max_length=120)
    recipe_pic = models.ImageField(upload_to="images",default='default.png')
    country = models.CharField(max_length=50)
    procedure = models.TextField('Instructions')
    guests_served = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    recipe_rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name
    
    def save_recipe(self):
        self.save()

    def delete_recipe(self):
        self.delete()
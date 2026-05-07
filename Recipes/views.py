from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'Recipes/Recipes_List.html', {'all_recipes': all_recipes})
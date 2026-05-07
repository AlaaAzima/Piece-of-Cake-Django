from django.contrib import admin
from .models import Recipe, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1 

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    list_display = ('name', 'course') 
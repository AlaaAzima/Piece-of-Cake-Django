from django.db import models

class Recipe(models.Model):
    COURSE_CHOICES = [
        ('Appetizers', 'Appetizers'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
    ]
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    description = models.TextField()
    #image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.quantity})"
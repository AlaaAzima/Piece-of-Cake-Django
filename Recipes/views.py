from .models import Recipe
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        cp = request.POST.get('confirm_password')
        role = request.POST.get('role')  # Catch the dropdown value

        if p != cp:
            messages.error(request, "Passwords do not match!")
            return render(request, 'Sign_up.html')

        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'Sign_up.html')

        # 1. Create the user
        new_user = User.objects.create_user(username=u, email=e, password=p)

        # 2. Assign Role
        if role == 'admin':
            new_user.is_staff = True  # This allows them to Add/Edit in /admin
            new_user.is_superuser = True  # Gives them full permissions

        new_user.save()

        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, 'Sign_up.html')
def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'log_in.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def recipe_list(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'Recipes/Recipes_List.html', {'all_recipes': all_recipes})

def home_view(request):
    return render(request, 'Recipes/Recipes_List.html')
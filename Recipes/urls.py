from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from Recipes import views  # Import from your specific app folder

urlpatterns = [
    path('admin/', admin.site.urls), # Re-enabling this for the team
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.recipe_list, name='recipe_list'),
    path('favorites/', views.home_view, name='favorites'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-food/', views.add_food_item, name='add_food_item'),
    path('log-intake/', views.log_intake, name='log_intake'),
    path('food-items/', views.food_items, name='food_items'),
    path('delete-food/<int:item_id>/', views.delete_food_item, name='delete_food_item'),
    path('delete-intake/<int:intake_id>/', views.delete_intake, name='delete_intake'),
    path('reset-calories/', views.reset_daily_calories, name='reset_daily_calories'),
]
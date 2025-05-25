from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-food/', views.addfood, name='addfood'),
    path('log/', views.log, name='log'),
    path('fooditems/', views.fooditems, name='fooditems'),
    path('delete-food/<int:item_id>/', views.delete_food_item, name='delete_food_item'),
    path('delete-intake/<int:intake_id>/', views.delete_intake, name='delete_intake'),
    path('reset-calories/', views.reset_daily_calories, name='reset_daily_calories'),
]
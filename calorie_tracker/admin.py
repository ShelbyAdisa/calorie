from django.contrib import admin
from .models import FoodItem, DailyIntake, UserProfile

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories_per_serving', 'category', 'created_at']  # Changed 'date_added' to 'created_at'
    list_filter = ['category', 'created_at']  # Changed 'date_added' to 'created_at'
    search_fields = ['name', 'brand']
    ordering = ['name']

@admin.register(DailyIntake)
class DailyIntakeAdmin(admin.ModelAdmin):
    list_display = ['food_item', 'servings', 'total_calories', 'intake_date', 'intake_time']  # Fixed all field names
    list_filter = ['intake_date']  # Changed 'date_consumed' to 'intake_date'
    search_fields = ['food_item__name']
    ordering = ['-intake_date', '-intake_time']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'daily_calorie_goal', 'current_weight', 'target_weight', 'activity_level']
    list_filter = ['activity_level', 'gender']
    search_fields = ['user__username', 'user__email']
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ('fruits', 'Fruits'),
        ('vegetables', 'Vegetables'),
        ('grains', 'Grains'),
        ('protein', 'Protein'),
        ('dairy', 'Dairy'),
        ('fats', 'Fats'),
        ('snacks', 'Snacks'),
        ('beverages', 'Beverages'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    calories_per_serving = models.DecimalField(max_digits=8, decimal_places=2)
    serving_size = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class DailyIntake(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    servings = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    total_calories = models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    intake_date = models.DateField(auto_now_add=True)
    intake_time = models.TimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Auto-calculate total calories
        if self.food_item:
            self.total_calories = Decimal(str(self.servings)) * self.food_item.calories_per_serving
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.food_item.name} - {self.servings} servings on {self.intake_date}"
    
    class Meta:
        ordering = ['-intake_date', '-intake_time']

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary (little/no exercise)'),
        ('light', 'Light (light exercise 1-3 days/week)'),
        ('moderate', 'Moderate (moderate exercise 3-5 days/week)'),
        ('active', 'Active (hard exercise 6-7 days/week)'),
        ('extra_active', 'Extra Active (very hard exercise, physical job)'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_calorie_goal = models.IntegerField(default=2000)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    target_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True, help_text="Height in centimeters")
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default='moderate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
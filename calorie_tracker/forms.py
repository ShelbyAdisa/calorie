from django import forms
from .models import FoodItem, DailyIntake

class FoodItemForm(forms.ModelForm):
    """
    Form for adding new food items to the database
    """
    class Meta:
        model = FoodItem
        fields = ['name', 'calories_per_serving', 'serving_size']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter food name'
            }),
            'calories_per_serving': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter calories per serving'
            }),
            'serving_size': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., 1 cup, 100g, 1 piece'
            })
        }

class DailyIntakeForm(forms.ModelForm):
    """
    Form for logging daily food intake
    """
    class Meta:
        model = DailyIntake
        fields = ['food_item', 'servings']  # Changed 'quantity' to 'servings'
        widgets = {
            'food_item': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'servings': forms.NumberInput(attrs={  # Changed 'quantity' to 'servings'
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'min': '0.1',
                'step': '0.1',
                'value': '1.0'
            })
        }
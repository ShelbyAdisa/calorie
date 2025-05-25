from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import FoodItem, DailyIntake
from .forms import FoodItemForm, DailyIntakeForm

def dashboard(request):
    """
    Main dashboard view displaying today's calorie intake and recent entries
    """
    today = timezone.now().date()
    
    # Get today's intake entries
    today_intakes = DailyIntake.objects.filter(intake_date=today)  # Changed from date_consumed
    
    # Calculate total calories for today - using the field directly, not a method
    total_calories = sum(intake.total_calories for intake in today_intakes)  # Removed () after total_calories
    
    # Get recent food items for quick access
    recent_foods = FoodItem.objects.all()[:10]
    
    context = {
        'today_intakes': today_intakes,
        'total_calories': total_calories,
        'recent_foods': recent_foods,
        'today': today,
    }
    
    return render(request, 'dashboard.html', context)

def addfood(request):
    """
    View for adding new food items to the database
    """
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('dashboard')
    else:
        form = FoodItemForm()
    
    return render(request, 'addfood.html', {'form': form})

def log(request):
    """
    View for logging daily food intake
    """
    if request.method == 'POST':
        form = DailyIntakeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food intake logged successfully!')
            return redirect('dashboard')
    else:
        form = DailyIntakeForm()
    
    return render(request, 'log.html', {'form': form})

def fooditems(request):
    """
    View to display all food items
    """
    items = FoodItem.objects.all()
    return render(request, 'fooditems.html', {'fooditems': items})

def delete_food_item(request, item_id):
    """
    View to delete a food item
    """
    item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, f'{item.name} has been deleted successfully!')
        return redirect('fooditems')
    
    return render(request, 'confirm_delete.html', {'item': item})

def delete_intake(request, intake_id):
    """
    View to delete an intake entry
    """
    intake = get_object_or_404(DailyIntake, id=intake_id)
    if request.method == 'POST':
        intake.delete()
        messages.success(request, 'Intake entry deleted successfully!')
        return redirect('dashboard')
    
    return render(request, '/confirm_delete_intake.html', {'intake': intake})

def reset_daily_calories(request):
    """
    View to reset today's calorie count
    """
    if request.method == 'POST':
        today = timezone.now().date()
        deleted_count = DailyIntake.objects.filter(intake_date=today).delete()[0]  # Changed from date_consumed
        messages.success(request, f'Reset complete! Removed {deleted_count} entries for today.')
        return redirect('dashboard')
    
    return render(request, 'confirm_reset.html')
from django.urls import path
from . import views

urlpatterns = [
    path('users/add/', views.add_user),
    path('users/', views.get_users),
    path('users/update/<int:id>/', views.update_user),
    path('users/delete/<int:id>/', views.delete_user),
    
    path('income/add/', views.add_income),
    path('income/', views.get_incomes),
    path('income/update/<int:id>/', views.update_income),
    path('income/delete/<int:id>/', views.delete_income),
    
    path('expenses/add/', views.add_expense),
    path('expenses/', views.get_expenses),
    path('expenses/update/<int:id>/', views.update_expense),
    path('expenses/delete/<int:id>/', views.delete_expense),
    
    path('categories/add/', views.add_category),
    path('categories/', views.get_categories),
    path('categories/update/<int:id>/', views.update_category),
    path('categories/delete/<int:id>/', views.delete_category),
    
    path('budgets/add/', views.add_budget),
    path('budgets/', views.get_budgets),
    path('budgets/update/<int:id>/', views.update_budget),
    path('budgets/delete/<int:id>/', views.delete_budget),
]

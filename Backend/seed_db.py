import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command
from api.models import User, Income, Expense, Category, Budget

def seed():
    print("Running database migrations...")
    call_command('makemigrations', 'api')
    call_command('migrate')

    print("Adding sample testing data...")

    # User
    User.objects.get_or_create(
        user_id=101,
        defaults={
            "full_name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "phone": "9876543210",
            "password": "rahul123",
            "city": "Hyderabad"
        }
    )

    # Income
    Income.objects.get_or_create(
        income_id=201,
        defaults={
            "user_name": "Rahul Sharma",
            "source": "Salary",
            "amount": 60000.00,
            "received_date": "2026-07-01",
            "description": "Monthly Salary"
        }
    )

    # Expense
    Expense.objects.get_or_create(
        expense_id=301,
        defaults={
            "user_name": "Rahul Sharma",
            "category": "Food",
            "amount": 450.00,
            "expense_date": "2026-07-05",
            "payment_method": "UPI",
            "description": "Lunch at Restaurant"
        }
    )

    # Category
    Category.objects.get_or_create(
        category_id=401,
        defaults={
            "category_name": "Food",
            "monthly_limit": 8000.00,
            "description": "Daily meals and dining"
        }
    )

    # Budget
    Budget.objects.get_or_create(
        budget_id=501,
        defaults={
            "user_name": "Rahul Sharma",
            "month": "July 2026",
            "total_income": 60000.00,
            "total_expense": 35000.00,
            "savings": 25000.00,
            "budget_status": "Under Budget"
        }
    )

    print("Seeding completed successfully!")

if __name__ == '__main__':
    seed()

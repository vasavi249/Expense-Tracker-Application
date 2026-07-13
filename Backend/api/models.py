from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    received_date = models.DateField()
    description = models.TextField(blank=True, null=True)

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expense_date = models.DateField()
    payment_method = models.CharField(max_length=50) # Cash, UPI, Debit Card, Credit Card, Net Banking
    description = models.TextField(blank=True, null=True)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    monthly_limit = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)

class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    month = models.CharField(max_length=50)
    total_income = models.DecimalField(max_digits=12, decimal_places=2)
    total_expense = models.DecimalField(max_digits=12, decimal_places=2)
    savings = models.DecimalField(max_digits=12, decimal_places=2)
    budget_status = models.CharField(max_length=50) # Under Budget, Over Budget

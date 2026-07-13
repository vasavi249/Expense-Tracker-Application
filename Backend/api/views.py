import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Income, Expense, Category, Budget

def parse_body(request):
    try:
        return json.loads(request.body)
    except:
        return {}

# ----------------- USER APIs -----------------
@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = parse_body(request)
        user = User.objects.create(**data)
        return JsonResponse({'message': 'User added', 'id': user.user_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_users(request):
    if request.method == 'GET':
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        User.objects.filter(user_id=id).update(**data)
        return JsonResponse({'message': 'User updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        User.objects.filter(user_id=id).delete()
        return JsonResponse({'message': 'User deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


# ----------------- INCOME APIs -----------------
@csrf_exempt
def add_income(request):
    if request.method == 'POST':
        data = parse_body(request)
        income = Income.objects.create(**data)
        return JsonResponse({'message': 'Income added', 'id': income.income_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_incomes(request):
    if request.method == 'GET':
        incomes = list(Income.objects.values())
        return JsonResponse(incomes, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_income(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Income.objects.filter(income_id=id).update(**data)
        return JsonResponse({'message': 'Income updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_income(request, id):
    if request.method == 'DELETE':
        Income.objects.filter(income_id=id).delete()
        return JsonResponse({'message': 'Income deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


# ----------------- EXPENSE APIs -----------------
@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = parse_body(request)
        expense = Expense.objects.create(**data)
        return JsonResponse({'message': 'Expense added', 'id': expense.expense_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_expenses(request):
    if request.method == 'GET':
        expenses = list(Expense.objects.values())
        return JsonResponse(expenses, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_expense(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Expense.objects.filter(expense_id=id).update(**data)
        return JsonResponse({'message': 'Expense updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_expense(request, id):
    if request.method == 'DELETE':
        Expense.objects.filter(expense_id=id).delete()
        return JsonResponse({'message': 'Expense deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


# ----------------- CATEGORY APIs -----------------
@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data = parse_body(request)
        category = Category.objects.create(**data)
        return JsonResponse({'message': 'Category added', 'id': category.category_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_categories(request):
    if request.method == 'GET':
        categories = list(Category.objects.values())
        return JsonResponse(categories, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_category(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Category.objects.filter(category_id=id).update(**data)
        return JsonResponse({'message': 'Category updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_category(request, id):
    if request.method == 'DELETE':
        Category.objects.filter(category_id=id).delete()
        return JsonResponse({'message': 'Category deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)


# ----------------- BUDGET APIs -----------------
@csrf_exempt
def add_budget(request):
    if request.method == 'POST':
        data = parse_body(request)
        budget = Budget.objects.create(**data)
        return JsonResponse({'message': 'Budget added', 'id': budget.budget_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_budgets(request):
    if request.method == 'GET':
        budgets = list(Budget.objects.values())
        return JsonResponse(budgets, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_budget(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Budget.objects.filter(budget_id=id).update(**data)
        return JsonResponse({'message': 'Budget updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_budget(request, id):
    if request.method == 'DELETE':
        Budget.objects.filter(budget_id=id).delete()
        return JsonResponse({'message': 'Budget deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

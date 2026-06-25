from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Expense, Income, Category, Budget
from .forms import ExpenseForm, IncomeForm, BudgetForm, CategoryForm
from django.db.models import Sum
from .services import get_budget_alerts, get_dashboard_summary
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            raw_name = form.cleaned_data['name'].strip()
            category = form.save(commit=False)
            category.user = request.user
            if Category.objects.filter(user =request.user, name__iexact = raw_name).exists():
                form.add_error('name', 'This Category already exists')
            else:
                category.save()
                return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'expenses/add_category.html',{'form': form})

@never_cache
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user= request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(user= request.user)

    return render(request, 'expenses/add_expenses.html', {'form': form})

@never_cache
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user = request.user).order_by('-date')

    search_query = request.GET.get('search')

    if search_query:
        expenses = expenses.filter(Q(description__icontains=search_query) | Q(category__name__icontains=search_query))
    
    category_id = request.GET.get('category')
    if category_id:
        expenses = expenses.filter(category_id=category_id)
        
    categories = Category.objects.filter(user=request.user)

    return render(request, 'expenses/expenses_list.html', {'expenses': expenses, 'categories': categories})

@never_cache
@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
        
    else:
        form = ExpenseForm(instance=expense, user= request.user)

    return render(request, 'expenses/edit_expenses.html', {'form': form})

@never_cache
@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

@never_cache
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
        
    else:
        form = IncomeForm()

    return render(request, 'expenses/add_income.html', {'form': form})

@never_cache
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    search_query = request.GET.get('search')
    if search_query:
        incomes = incomes.filter(Q(source__icontains= search_query) | Q(amount__icontains=search_query))
    total_income = incomes.aggregate(total =Sum('amount'))['total'] or 0
    return render(request, 'expenses/income_list.html', {'incomes': incomes, 'total': total_income})
    
@never_cache
@login_required
def dashboard(request):
    summary = get_dashboard_summary(request.user)
    
    alerts = get_budget_alerts(request.user)
    context = {'total_expense': summary['total_expense'], 'expenses': summary['recent_expenses'],'total_income': summary['total_income'], 'savings': summary['savings'], 'category_data': summary['category_data'], 'alerts': summary['alerts']}

    return render(request, 'expenses/dashboard.html', context)

@never_cache
@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST, user=request.user)
        if form.is_valid():
            
            category_obj = form.cleaned_data['category'] 
            month_date = form.cleaned_data['month']      
            if Budget.objects.filter(user=request.user, category=category_obj, month=month_date).exists():
                form.add_error('category', f'A budget for {category_obj.name} already exists for this month.')
            else:
                budget = form.save(commit=False)
                budget.user = request.user
                budget.save()
                return redirect('budget')
    else:
        form = BudgetForm(user=request.user)
        
    return render(request, 'expenses/add_budget.html', {'form': form})

@never_cache
@login_required
def view_budget(request):

    budgets = Budget.objects.filter(user = request.user).order_by('-month')
    for budget in budgets:      
        total_spent = Expense.objects.filter(
            user=request.user,
            category=budget.category,
            date__year=budget.month.year,
            date__month=budget.month.month
        ).aggregate(total=Sum('amount'))['total'] or 0
        budget.spent = total_spent
        budget.percentage = (total_spent / budget.limit)*100
    context = {'budgets': budgets}
    return render(request, 'expenses/budgets_list.html', context)

@never_cache
@login_required
def delete_category(request, pk):

    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    
    return render(request, 'expenses/delete_category.html', {'category': category})

@never_cache
@login_required
def category_list(request):
    categories = Category.objects.filter(user = request.user)

    context = {'categories': categories}
    return render(request, 'expenses/category_list.html', context)

@never_cache
@login_required
def delete_budget(request, pk):

    budget = get_object_or_404(Budget, pk=pk, user=request.user)

    if request.method == 'POST':
        budget.delete()
        return redirect('budget')
    
    return render(request, 'expenses/delete_budget.html', {'budget': budget})

@never_cache
@login_required
def delete_income(request, pk):

    income = get_object_or_404(Income, pk=pk, user=request.user)

    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    
    return render(request, 'expenses/delete_income.html', {'income': income})
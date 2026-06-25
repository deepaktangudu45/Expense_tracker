from django.db.models import Sum
from datetime import date
from .models import Expense, Budget, Income
import datetime


def get_budget_alerts(user):
    today = date.today()
    alerts = []

    budgets = Budget.objects.filter(
        user=user,
        month__year=today.year,
        month__month=today.month
    )

    for budget in budgets:
        spent = Expense.objects.filter(
            user=user,
            category=budget.category,
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum('amount'))['total'] or 0

        usage_percentage = (spent / budget.limit) * 100

        if usage_percentage >= 100:
            level = 'DANGER'
        elif usage_percentage >= 85:
            level = 'WARNING'
        else:
            continue  # No alert

        alerts.append({
            'category': budget.category.name,
            'budget': budget.limit,
            'spent': spent,
            'percentage': round(usage_percentage, 2),
            'level': level
        })

    return alerts

def get_dashboard_summary(user):
    today = datetime.date.today()
    month = today.month
    year = today.year

    expenses = Expense.objects.filter(user=user, date__month = month, date__year = year)

    incomes = Income.objects.filter(user=user, date__month = month, date__year = year)  

    total_expense = expenses.aggregate(total= Sum('amount'))['total'] or 0

    total_income = incomes.aggregate(total= Sum('amount'))['total'] or 0
    savings = total_income - total_expense  
    recent_expenses = Expense.objects.order_by('-date').filter(user = user, date__month = month, date__year = year)[:5]
    category_data = expenses.values('category__name').annotate(total=Sum('amount')).order_by('-total')
    alerts = get_budget_alerts(user)
    return {'total_expense': total_expense,
            'total_income': total_income,
            'savings': savings,
            'alerts': alerts,
            'recent_expenses': recent_expenses,
            'category_data': category_data}


from django.urls import path
from .views import ExpenseListAPI, CategoryListAPI, IncomeListAPI, dashboardSummaryAPI

urlpatterns = [
    path('expenses/', ExpenseListAPI.as_view(), name='api_expenses'),
    path('category/', CategoryListAPI.as_view(), name='api_categories'),
    path('incomes/', IncomeListAPI.as_view(), name='api_incomes'),
    path('dashboardSummary/', dashboardSummaryAPI.as_view(), name='dashboard_summary')
]

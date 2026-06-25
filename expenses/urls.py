from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:pk>/delete', views.delete_expense, name='delete_expense'),
    path('expenses/<int:pk>/edit', views.edit_expense, name='edit_expense'),
    path('income', views.income_list, name='income_list'),
    path('income/add', views.add_income, name='add_income'),
    path('income/<int:pk>/delete', views.delete_income, name='delete_income'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.add_category, name = 'add_category'),
    path('category/<int:pk>/delete', views.delete_category, name='delete_category'),
    path('budget/', views.view_budget, name ='budget'),
    path('budget/add/', views.add_budget, name= 'add_budget'),
    path('budget/<int:pk>/delete', views.delete_budget, name='delete_budget'),
    path('', views.dashboard, name = 'dashboard')
]

from rest_framework import serializers
from expenses.models import Expense, Category, Income

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Expense
        fields = ['id', 'category', 'description', 'amount', 'date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'source', 'amount', 'date']

class DashboardSerializer(serializers.Serializer):
    total_expense = serializers.DecimalField(max_digits=15, decimal_places=2)
    total_income = serializers.DecimalField(max_digits=15, decimal_places=2)
    savings = serializers.DecimalField(max_digits=15, decimal_places=2)
    recent_expenses = ExpenseSerializer(many =True)
    alerts = serializers.ListField()
    category_data = serializers.ListField()
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from expenses.models import Expense, Income, Category
from .serializers import ExpenseSerializer, IncomeSerializer, CategorySerializer, DashboardSerializer
from expenses.services import get_dashboard_summary


class ExpenseListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        expenses = Expense.objects.filter(user = request.user)
        serializer = ExpenseSerializer(expenses, many= True)
        return Response(serializer.data)
    
class IncomeListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        incomes = Income.objects.filter(user = request.user)
        serializer = IncomeSerializer(incomes, many= True)
        return Response(serializer.data)
    
class CategoryListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.filter(user = request.user)
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data)
    
class dashboardSummaryAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = get_dashboard_summary(user= request.user)
        serializer = DashboardSerializer(data)
        return Response(serializer.data)
    
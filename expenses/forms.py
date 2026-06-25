from django import forms    
from .models import Expense, Income, Budget, Category


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date', 'payment_method']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super(ExpenseForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

class BudgetForm(forms.ModelForm):
    month = forms.DateField(
        # 1. Setup the widget to show the Month Picker and display YYYY-MM
        widget=forms.DateInput(format='%Y-%m', attrs={'type': 'month'}),
        
        # 2. Tell Django to accept the "YYYY-MM" format when processing the form
        input_formats=['%Y-%m']
    )
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'month']
    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None) 
        super(BudgetForm, self).__init__(*args, **kwargs)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

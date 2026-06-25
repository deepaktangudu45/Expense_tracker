from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['user'])]

    def __str__(self):
        return self.name
        

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, related_name='expenses')
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),               
        ('card', 'Card'),               
        ('upi', 'UPI'),               
        ('cheque', 'Cheque')]
    
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField()
    date = models.DateField()
    payment_method = models.CharField(max_length=20,choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user','date']),
            models.Index(fields=['category'])
        ]

    def __str__(self):
        if self.category:
            return f"{self.category.name} - {self.amount}"
        return f"Uncategorized - {self.amount}"
    

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'date'])
        ]

    def __str__(self):
        return f"{self.user} - {self.source} - {self.amount}"
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    month = models.DateField(help_text='Use first day of the month as date')
    limit = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        unique_together = ('user', 'category', 'month')
        indexes = [models.Index(fields=['user', 'month'])]

    def __str__(self):
        return f"{self.category} - {self.limit} - {self.month}"
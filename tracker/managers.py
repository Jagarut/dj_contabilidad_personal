from django.db import models

# custom QuerySet class
# To use the custom QuerySet, you need to attach it to your model's manager
class TransactionQuerySet(models.QuerySet):
    def get_expenses(self):
        return self.filter(tipo='gasto')
    
    def get_income(self):
        return self.filter(tipo='ingreso')
    
    def get_total_expenses(self):
        gastos = self.get_expenses().aggregate(total=models.Sum('amount'))['total'] or 0
        
        return gastos
    
    def get_total_income(self):
        ingresos = self.get_income().aggregate(total=models.Sum('amount'))['total'] or 0
        
        return ingresos
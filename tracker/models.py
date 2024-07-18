from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import TransactionQuerySet

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name 

# transaction puede ser INGRESO ó GASTO
# has an amount
# has a CATEGORY (FK)
# is tied to a User (FK)
# has a DATE
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('ingreso', 'Ingreso'),
        ('gasto','Gasto'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    # custom manager that uses custom QuerySet.
    objects = TransactionQuerySet.as_manager()

    def __str__(self) -> str:
        return f"{self.tipo} de {self.amount} el {self.date} de {self.user}"
    
    class Meta:
        ordering = ['-date']
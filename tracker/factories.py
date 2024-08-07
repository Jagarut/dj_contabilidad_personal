from datetime import datetime
import factory
from tracker.models import Category, Transaction, User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: f'user{n}')

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('name',)

    name = factory.Iterator(
        [
            "Facturas",
            "Comida",
            "Ropa",
            "Médico",
            "Vivienda",
            "Sueldo",
            "Social",
            "Transporte",
            "Vacaciones",
        ]
    )

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction  # Equivalent to ``model = myapp.models.User``
        
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    amount = 5
    date = factory.Faker(
        'date_between',
        start_date=datetime(year=2022, month=1, day=1).date(),
        end_date=datetime.now().date()
    )
    tipo = factory.Iterator(
        [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
    )
    

import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category


class Command(BaseCommand):
    help = "Generates transactons for testing"

    def handle(self, *args, **options) -> str | None:
        fake = Faker()

        # create categories
        categories = [
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

        if Category.objects.count():
            Category.objects.all().delete()

        for category in categories:
            Category.objects.get_or_create(name=category)

        # get the user
        user = User.objects.filter(username="chus").first()
        if not user:
            user = User.objects.create_superuser(username="chus", password="chus")

        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]

        if Transaction.objects.count():
            Transaction.objects.all().delete()

        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date="-1y", end_date="today"),
                tipo=random.choice(types),
            )

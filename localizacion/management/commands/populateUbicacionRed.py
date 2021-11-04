from django.core.management import BaseCommand
from faker import Faker
from ubicacion_red.models import UbicacionRed
from random import randrange

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        for i in range(10):
            UbicacionRed.objects.create(
                idUser = faker.aba(),
                location= faker.bank_country()
            )

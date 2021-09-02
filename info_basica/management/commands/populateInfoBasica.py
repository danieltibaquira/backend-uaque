from django.core.management import BaseCommand
from faker import Faker
from info_basica.models import InfoBasica
from random import randrange

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        for i in range(10):
            InfoBasica.objects.create(
                idUser = faker.aba(),
                countryOfBirth = faker.bank_country(),
                stateOfBirth = faker.bank_country(),
                birthDate = faker.date(),
                maritalStatus = faker.job(),
                locality = faker.bank_country(),
                livesWith = faker.job(),
                works = faker.boolean(),
                schoolCity = faker.bank_country(),
                age = randrange(16, 99),
                gender = faker.prefix_nonbinary(),
            )

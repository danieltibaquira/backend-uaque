from django.core.management import BaseCommand
from random import randrange
from faker import Faker
from uso_biblioteca.models import LibUse
from uso_biblioteca.models import TranLib
from uso_biblioteca.models import LibRes
from uso_biblioteca.models import AzUse
from uso_biblioteca.models import TranAz
from uso_biblioteca.models import AzRes
from uso_biblioteca.models import RepoUse
from uso_biblioteca.models import TranRepo
from uso_biblioteca.models import RepoRes

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        for i in range(10):
            libUseSave = LibUse.objects.create(
                idUser=faker.aba()
            )

            TranLib.objects.create(
                idResource=faker.aba(),
                date=faker.date(),
                theme=faker.job(),
                libUse=libUseSave
            )

            LibRes.objects.create(
                idResource=faker.aba(),
                theme=faker.job(),
                dateCreated=faker.date(),
                copies=randrange(0, 100),
                typeRes=faker.job(),
                author=faker.name(),
                title=faker.title()
            )

            azUseSave = AzUse.objects.create(
                idUser=faker.aba()
            )

            TranAz.objects.create(
                idResource=faker.aba(),
                date=faker.date(),
                theme=faker.job(),
                azUse=azUseSave
            )

            AzRes.objects.create(
                idResource=faker.aba(),
                theme=faker.job(),
                dateCreated=faker.date(),
                url=faker.domain_name(),
                repo=faker.domain_name(),
                author=faker.name(),
                title=faker.title()
            )

            repoUseSave = RepoUse.objects.create(
                idUser=faker.aba()
            )

            TranRepo.objects.create(
                idResource=faker.aba(),
                date=faker.date(),
                theme=faker.job(),
                repoUse=repoUseSave
            )

            RepoRes.objects.create(
                idResource=faker.aba(),
                theme=faker.job(),
                dateCreated=faker.date(),
                faculty=faker.job(),
                program=faker.job(),
                repo=faker.domain_name(),
                author=faker.name(),
                title=faker.title()
            )

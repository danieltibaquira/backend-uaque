from django.core.management import BaseCommand
from faker import Faker
from info_academica.models import InfoAcademica
from info_academica.models import Schedule
from info_academica.models import AcademicGroup
from info_academica.models import RecreativeActivity

class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()
        for i in range(10):

            infoSave = InfoAcademica.objects.create(
                idUser = faker.aba(),
                faculty = faker.job(),
                program = faker.job(),
            )

            Schedule.objects.create(
                term=faker.date(),
                academicLevel=faker.job(),
                idProfessor = faker.aba(),
                info_acad = infoSave
            )
            AcademicGroup.objects.create(
                idDirector = faker.aba(),
                type = faker.job(),
                name = faker.name(),
                info_acad = infoSave
            )
            RecreativeActivity.objects.create(
                type = faker.job(),
                name = faker.name(),
                info_acad=infoSave
            )

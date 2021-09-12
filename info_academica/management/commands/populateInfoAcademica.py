from django.core.management import BaseCommand

import random
from django_seed import Seed
from faker import Faker
from info_academica.models import InfoAcademica
from info_academica.models import Schedule
from info_academica.models import AcademicGroup
from info_academica.models import RecreativeActivity


class Command(BaseCommand):
    def handle(self, *args, **options):
        seeder = Seed.seeder(locale='es_MX')
        faculty_array = [
            'ARQUITECTURA Y DISEÑO',
            'Artes',
            'Ciencias',
            'Ciencias Económicas y Administrativas',
            'Ciencias Jurídicas',
            'Ciencias Políticas y Relaciones Internacionales',
            'Ciencias Sociales',
            'Comunicación y Lenguaje',
            'Derecho Canónico',
            'Educación',
            'Enfermería',
            'Estudios Ambientales y Rurales',
            'Filosofía',
            'Ingeniería',
            'Medicina',
            'Odontología',
            'Psicología',
        ]

        seeder.add_entity(InfoAcademica, 5, {
            'idUser': lambda x: seeder.faker.aba(),
            'faculty': lambda x: random.choice(faculty_array),
            'program': lambda x: seeder.faker.job()
        })
        '''
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
            '''

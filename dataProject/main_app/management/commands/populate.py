import json
import os.path

from django.core.management import BaseCommand

from dataProject import settings
from main_app.models import Employee


class Command(BaseCommand):
    help = "Populates employees table with 1000 records"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, "employees.json")
        self.stdout.write(
            self.style.SUCCESS('Started to Import Data')
        )
        with open(path) as file:
            employees = json.load(file)
            for e in employees:
                Employee.objects.create(
                    name=e['name'],
                    email=e['email'],
                    dob=e['dob'],
                    salary=e['salary'],
                    disabled=e['disbled']
                )
        self.stdout.write(
            self.style.SUCCESS('Completed Importing Data')
        )


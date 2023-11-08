from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Populates employees table with 1000 records"

    def handle(self, *args, **options):
        pass

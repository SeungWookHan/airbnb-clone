from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command create many facilites"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many times do you want me to tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        facilites = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilites:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilites)} facilites created'))

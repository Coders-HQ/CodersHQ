from django.core.management.base import BaseCommand, CommandError
from codershq.challenge.models import Challenge
from django.utils import timezone


class Command(BaseCommand):
    help = 'Ends challenge and updates all users'

    def handle(self, *args, **options):
        for challenge in Challenge.objects.all():

            if challenge.date_end == timezone.localtime().date():
                for competitor in challenge.competitors.all():
                    competitor.completed_challenges += 1
                    competitor.save()

        self.stdout.write(self.style.SUCCESS('Successfully checked challenge'))

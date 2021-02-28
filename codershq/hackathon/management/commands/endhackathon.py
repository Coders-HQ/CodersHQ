from django.core.management.base import BaseCommand, CommandError
from codershq.hackathon.models import Hackathon
from django.utils import timezone


class Command(BaseCommand):
    help = 'Ends hackathon and updates all users'


    def handle(self, *args, **options):
        for hackathon in Hackathon.objects.all():
            
            if hackathon.date_end == timezone.localtime().date():
                for competitor in hackathon.competitors.all():
                    competitor.completed_hackathons += 1
                    competitor.save()

        self.stdout.write(self.style.SUCCESS('Successfully checked hackathon'))
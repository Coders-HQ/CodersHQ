from codershq.hackathon.models import Hackathon
from django.utils import timezone
from config import celery_app



@celery_app.task()
def update_hackathon():
    for hackathon in Hackathon.objects.all():

        if hackathon.date_end == timezone.localtime().date():
            for competitor in hackathon.competitors.all():
                competitor.completed_hackathons += 1
                competitor.save()

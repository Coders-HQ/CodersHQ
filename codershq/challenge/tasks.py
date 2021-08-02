from codershq.challenge.models import Challenge
from django.utils import timezone
from config import celery_app


@celery_app.task()
def update_challenge():
    for challenge in Challenge.objects.all():

        if challenge.date_end == timezone.localtime().date():
            for competitor in challenge.competitors.all():
                competitor.completed_challenges += 1
                competitor.save()

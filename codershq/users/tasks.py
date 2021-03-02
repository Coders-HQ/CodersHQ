from django.contrib.auth import get_user_model
from django.conf import settings
from codershq.users.scoring.score import CHQScore
from celery.utils.log import get_task_logger
from config import celery_app

logger = get_task_logger(__name__)

User = get_user_model()

# @celery_app.task()
# def get_users_count():
#     """A pointless Celery task to demonstrate usage."""
#     return User.objects.count()
# @celery_app.task()
# def get_users_count():
#     """A pointless Celery task to demonstrate usage."""
#     return User.objects.count()

@celery_app.task()
def update_github_score(pk):
    """
    update_github_score update user's github score using
    the scoring system

    :param pk: user's primary key
    """
    user = User.objects.get(pk=pk)
    chq_score = CHQScore(settings.GITHUB_TOKEN)

    # try to get score
    try:
        user.github_score, user.fav_language = chq_score.get_score(user.github_username)
        user.github_updated = timezone.now()
    except:
        # use old score (or 0) if api call fails
        print("couldnt save")

    # make sure the data is good and save
    user.full_clean()
    user.save()
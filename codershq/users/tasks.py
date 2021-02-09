from django.contrib.auth import get_user_model
from django.conf import settings
# from codershq.users.scoring.score import CHQScore

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

# @celery_app.task()
# def update_github_score():
#     """
#     update_github_score takes user_name and id of user profile
#     and saves the user score to the profile.
#     This is an async functions

#     :param user_name: github username
#     :param id: profile id
#     :param old_score: get back old score if error getting new score
#     """


#     # # try to get score
#     # try:
#     #     chq_score = CHQScore(settings.GITHUB_TOKEN)
#     #     User.github_score = chq_score.get_score(User.github_username)
#     #     User.github_updated = timezone.now()
#     # except:
#     #     # use old score (or 0) if api call fails
#     #     logger.info("unable to get score")
#     #     User.github_score = old_score

#     # # make sure the data is good and save
#     # User.full_clean()
#     # User.save()
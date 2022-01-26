from allauth.account.models import EmailAddress
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from codershq.challenge.models import Challenge
from codershq.challenge.slack import create_channel


def send_challenge_mail(sender, **kwargs):
    if kwargs.get("action") == "post_add":
        email = EmailAddress.objects.get(pk=list(kwargs["pk_set"])[0])
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [email],
            fail_silently=True,
        )


# m2m_changed.connect(send_challenge_mail, sender=Challenge.competitors.through)


# @receiver(post_save, sender=Challenge)
# def create_slack_channel(sender, instance, created, **kwargs):
#     # creates slack channel using slack api

#     # check if slack token is available
#     if settings.SLACK_TOKEN != "":

#         # if a challenge is created
#         if created:
#             # create slack channel
#             create_channel(instance.slug)

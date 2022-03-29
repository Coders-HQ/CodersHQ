from allauth.account.models import EmailAddress
from django.core.mail import send_mail


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

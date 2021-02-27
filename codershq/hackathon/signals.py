from django.db.models.signals import m2m_changed
from codershq.hackathon.models import Hackathon
from allauth.account.models import EmailAddress
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from codershq.hackathon.slack import create_channel

def send_hackathon_mail(sender, **kwargs):
    if kwargs.get('action') == 'post_add': 
        email = EmailAddress.objects.get(pk=list(kwargs['pk_set'])[0])
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            [email],
            fail_silently=True,
        )
    
m2m_changed.connect(send_hackathon_mail, sender=Hackathon.competitors.through)

@receiver(post_save, sender=Hackathon)
def create_slack_channel(sender, instance, created, **kwargs):
    if created:
        create_channel(instance.slug)
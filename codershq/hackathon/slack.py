import slack
from django.conf import settings

def create_channel(channel):
    client = slack.WebClient(token=settings.SLACK_TOKEN)
    client.conversations_create(name=channel)
import slack
from django.conf import settings

def create_channel(channel):
    """create slack channel once a new hackathon is created"""

    client = slack.WebClient(token=settings.SLACK_TOKEN)
    client.conversations_create(name=channel)
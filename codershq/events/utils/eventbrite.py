from django.conf import settings
from datetime import datetime, timedelta, timezone
import requests
from dataclasses import dataclass, field
import pytz

from codershq.events.models import Event
from attrdict import AttrDict


@dataclass()
class Eventbrite:
    # base url of eventbrite api
    BASE_URL = "https://www.eventbriteapi.com/v3"

    """ required event fields to create an event """
    title: str = ""
    start_datetime: datetime = field(default_factory=datetime.now(tz=timezone.utc))
    duration: int = 0
    currency: str = ""

    """ optional, implemented event fields used to describe the event """
    description: str = ""
    # event summary should be max 140 characters
    summary: str = ""
    # event requirements can include PCR, vaccine, etc
    requirements: str = ""
    # event link for online events
    link: str = ""
    # event location for face-to-face events
    location: str = ""
    # number of available seats or tickets
    seats: int = 0

    """ optional, not yet implemented event fields used to describe the event """
    # if true, event is online and does not have a venue
    is_online_event: bool = False
    # if true, event is publicly searchable on Eventbrite website
    is_listed: bool = False
    # if true, event is shareable; social sharing buttons are included for the event on Eventbrite
    is_shareable: bool = False
    # if true, only invitees who received an invitation email can see event on Eventbrite
    is_invite_only: bool = False
    # if true, displays the total number of remaining event tickets
    show_remaining: bool = False
    # event password entered by visitors to access event details
    password: str = ""

    end_datetime = start_datetime + timedelta(hours=duration)

    body = {
        "event": {
        "name": {
          "html": title
        },
        "description": {
          "html": description
        },
        "start": {
          "timezone": start_datetime.tzname(),
          "utc": start_datetime
        },
        "end": {
           "timezone": end_datetime.tzname(),
           "utc": end_datetime
        },
        "currency": currency,
        "online_event": is_online_event,
        "organizer_id": settings.EVENTBRITE_ORGANIZATION_ID,
        "listed": is_listed,
        "shareable": is_shareable,
        "invite_only": is_invite_only,
        "show_remaining": show_remaining,
        "password": password,
        "capacity": seats
        }
    }

    body = AttrDict(body)

    # TODO: text and img modules

    @classmethod
    def create_event(cls, chq_event: Event):
        # TODO: error message for instance creation failure
        event_instance = cls(title=chq_event.title, start_date_time=chq_event.date_time,
                             duration=chq_event.duration, summary=chq_event.short_description,
                             description=chq_event.description, requirements=chq_event.requirements,
                             link=chq_event.event_link, location=chq_event.event_location, seats=chq_event.seats)

        event_id = event_instance.post_basic_info()

        return event_instance

    def post_basic_info(self):
        url = f'{Eventbrite.BASE_URL}/organizations/{settings.EVENTBRITE_ORGANIZATION_ID}/events/'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
            'Accept': 'application/json',
        }

        self.body.event.name.html = self.title
        '''///'''

        response = requests.post(url=url, headers=headers, json=self.body)

        event_id = response.json()["id"]

        return event_id




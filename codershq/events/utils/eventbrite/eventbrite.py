from django.conf import settings
from datetime import datetime, timedelta, timezone
import requests
from dataclasses import dataclass, field
import sys
# import pytz


from event import EventbriteEvent
from ticket import EventbriteTicket


@dataclass()
class Eventbrite:
    # base url of eventbrite api
    BASE_URL = "https://www.eventbriteapi.com/v3"

    @staticmethod
    def event_handler(chq_event, chq_tickets=None, event_id: str = None):
        """
            if an event id is passed, update the event
            else, create the event and return event_id
        """

        if event_id:
            EventbriteEvent.update_event(chq_event=chq_event, event_id=event_id)

        else:
            event_id = EventbriteEvent.create_event(chq_event=chq_event, chq_tickets=chq_tickets)
            return event_id


    @staticmethod
    def post_request(url, body=None) -> dict:
        """
            send a post request to eventbrite api
        """

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
            'Content-Type': 'application/json',
        }

        # choose between sending a post request with a body or without
        if body:
            response = requests.post(url=url, headers=headers, json=body)
        else:
            response = requests.post(url=url, headers=headers)

        response = response.json()

        # display an error if post request to Eventbrite api failed
        if response.get("status_code"):
            print("ERROR "+ str(response["status_code"]) +": Post request to Eventbrite failed - "+ response["error_description"])
            return {}

        return response


    @staticmethod
    def delete_request(url) -> dict:
        """
            send a delete request to eventbrite api
        """

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
        }

        response = requests.delete(url=url, headers=headers)

        response = response.json()

        if response.get("status_code"):
            print("ERROR "+ str(response["status_code"]) +": Delete request to Eventbrite failed - "+ response["error_description"])
            return {}

        return response



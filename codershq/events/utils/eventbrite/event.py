from django.conf import settings
from datetime import datetime, timedelta, timezone
import requests
from dataclasses import dataclass, field
import sys
# import pytz

from eventbrite import Eventbrite
from ticket import EventbriteTicket


@dataclass()
class EventbriteEvent:
    # TODO: add text and img support modules

    """ required event fields to create an event """
    name: str = ""
    start_date_time: datetime = field(default_factory=datetime.now(tz=timezone.utc)+timedelta(minutes=1))
    end_date_time: datetime = field(default_factory=start_date_time)
    currency: str = "USD"  # currently AED currency is not supported, as per testing

    """ optional, implemented event fields used to describe the event """
    description: str = ""
    # event summary should be max 140 characters
    summary: str = ""
    # event requirements can include PCR, vaccine, etc
    requirements: str = ""
    # event location for face-to-face events
    location: str = ""
    # number of available seats/tickets
    capacity: int = 0

    """ optional, not yet implemented event fields used to describe the event """
    # if true, event is online and does not have a venue
    is_online_event: bool = False
    # if true, event is publicly searchable on Event website
    is_listed: bool = False
    # if true, event is shareable; social sharing buttons are included for the event on Event
    is_shareable: bool = False
    # if true, only invitees who received an invitation email can see event on Event
    is_invite_only: bool = False
    # if true, displays the total number of remaining event tickets
    show_remaining: bool = False
    # event password entered by visitors to access event details
    # set if you want only visitors with the password to signup for the event
    password: str = ""

    # store all ticket ids linked to the event
    ticket_ids: list = field(default_factory=list)


    """
        class methods below
    """
    @classmethod
    def create_event(cls, chq_event, chq_tickets=None) -> str:
        """
        TODO: add text and img support modules

        TODO: Missing ticket information in Event Model: number of ticket types, name of ticket type,
              ticket quantity of each type, is the ticket free?, if ticket is not free what is the cost and currency

        TODO: check if date_time received from event model will reflect correctly on eventbrite. Since it might
              not be in UTC, it might behave differently.

        TODO: error handling for instance creation failure
        """

        """
            Helps create and display an event on eventbrite by doing the following:
                1- sending a post request containing the event details
                2- sending a post request containing at least one ticket type of the event
                3- sending a post request to publish the event details on eventbrite -
                    To make it visible to the public, set ${is_listed} to True
        """

        # create an event instance
        event_instance = cls(
            name=chq_event.name, 
            start_date_time=chq_event.start,
            end_date_time=chq_event.start, 
            summary=chq_event.summary, # not being used in defining event body, consider removing it
            description=chq_event.description,
            location=chq_event.event_location, 
            capacity=chq_event.capacity
            )
        
        # send the event details to eventbrite api
        url = f'{Eventbrite.BASE_URL}/organizations/{settings.EVENTBRITE_ORGANIZATION_ID}/events/'

        post_event_response = event_instance.post_event_details(url=url)

        # display an error if sending event details to eventbrite api failed
        if not post_event_response:
            print("ERROR: Failed to create event - Couldn't post event details to Eventbrite")

            del event_instance
            print("INFO: Successfully deleted event instance created in system")

            return ""

        # get the event id from the post response received
        event_id = post_event_response["id"]

        # TODO: Include support for when chq_tickets is defined.
        #       Make sure to include support for when more than one type of ticket is defined.

        # if chq_tickets is not defined, define a default free ticket
        # at least one ticket must be defined to create an event - Requirement by Eventbrite
        if not chq_tickets:
            ticket_id = EventbriteTicket.create_ticket(event_id=event_id, ticket_type="FREE",
            ticket_quantity=500, ticket_is_free=True, ticket_currency=event_instance.currency)

            if not ticket_id:
                print("ERROR: Couldn't get a ticket id - Failed to create ticket")
                return ""

        # add the ticket id to the event
        event_instance.ticket_ids.append(ticket_id)

        # publish the event on eventbrite
        publish_event_response = EventbriteEvent.publish_event(event_id=event_id)

        # display an error if sending a publish request to eventbrite api failed
        if not publish_event_response:
            print("ERROR: Failed to publish event - Event is created on Eventbrite but is not published")
            return ""        

        print("INFO: Successfully created and published the event to Eventbrite")

        return event_id


    @classmethod
    def update_event(cls, chq_event, event_id: str) -> None:

        # create an event instance with both old and new event details
        event_instance = cls(
            name=chq_event.name, 
            start_date_time=chq_event.start,
            end_date_time=chq_event.start, 
            summary=chq_event.summary, # not being used in defining event body, consider removing it
            description=chq_event.description,
            location=chq_event.event_location, 
            capacity=chq_event.capacity
            )
        
        # get the updated event body
        updated_event_body = event_instance.get_event_body()

        # send the updated event details to eventbrite
        url = f'{Eventbrite.BASE_URL}/events/{event_id}/'
        post_response = Eventbrite.post_request(url=url, body=updated_event_body)

        if not post_response:
            print("ERROR: Failed to update event - Couldn't post event details to eventbrite")

            del event_instance
            print("INFO: Successfully deleted event instance created in system")

            return

        print("INFO: Successfully updated the event on Eventbrite")


    """
        static methods below
    """
    @staticmethod
    def publish_event(event_id: str) -> dict:
        """
            Used to publish the event on eventbrite
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}/publish/'

        response = Eventbrite.post_request(url=url)

        # display an error if publishing an event failed
        if not response:
            print("ERROR: Failed to publish the event on Eventbrite - Event is created with its ticket(s) but is not published")
            return {}

        print("INFO: Successfully sent a post request to Eventbrite to publish event.")

        return response


    @staticmethod
    def delete_event(event_id: str) -> dict:
        """
            Used to delete event specified by ${event_id}
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}'

        response = Eventbrite.delete_request(url=url)

        if not response:
            print("ERROR: Failed to delete event on Eventbrite")
            return {}

        print("INFO: Successfully deleted the event from Eventbrite")

        return response


    """
        instance methods below
    """
    def get_event_body(self) -> dict:
        """
            define and return the event body dictionary based on event details
        """

        event_body = {
            "event": {
                "name": {
                    "html": self.name
                },
                "description": {
                    "html": self.description
                },
                "start": {
                    "timezone": 'UTC',
                    "utc": self.start_date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
                },
                "end": {
                    "timezone": 'UTC',
                    "utc": self.end_date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
                },
                "currency": self.currency,
                "online_event": self.is_online_event,
                "listed": self.is_listed,
                "shareable": self.is_shareable,
                "invite_only": self.is_invite_only,
                "show_remaining": self.show_remaining,
                "password": self.password,
                "capacity": self.capacity
            }
        }

        return event_body


    def post_event_details(self, url) -> dict:
        """
            send a post request to eventbrite api with the event details
        """

        event_body = self.get_event_body()

        response = Eventbrite.post_request(url=url, body=event_body)

        # display an error if sending event details to eventbrite api failed
        if not response:
            print("ERROR: Failed to post event details on Eventbrite - Event is not created")
            return {}

        print("INFO: Successfully posted event details on eventbrite.")

        return response

from django.conf import settings
from datetime import datetime, timedelta, timezone
import requests
from dataclasses import dataclass, field
import sys
# import pytz


@dataclass()
class Eventbrite:
    # TODO: add text and img support modules

    # base url of eventbrite api
    BASE_URL = "https://www.eventbriteapi.com/v3"

    """ required event fields to create an event """
    title: str = ""
    start_datetime = datetime.now(tz=timezone.utc)
    duration: int = 0
    currency: str = "USD"  # currently AED currency is not supported, as per testing

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
    # number of available seats/tickets
    seats: int = 0

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
    ticket_ids: list[str] = field(default_factory=list)

    @classmethod
    def create_event(cls, chq_event):
        """
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

        event_instance = cls(title=chq_event.title, start_date_time=chq_event.date_time,
                             duration=chq_event.duration, summary=chq_event.short_description,
                             description=chq_event.description, requirements=chq_event.requirements,
                             link=chq_event.event_link, location=chq_event.event_location, seats=chq_event.seats)

        post_event_response = event_instance.post_basic_info()

        event_id = post_event_response["id"]

        # create at least one event ticket
        # TODO: change below default ticket info. Could add a loop to create more than one ticket based on number
        #       of ticket types argument
        ticket_id = EventbriteTicket.create_ticket(event_id=event_id, ticket_type="FREE",
                                                   ticket_quantity=event_instance.seats, ticket_is_free=True)

        # add the ticket id to the event
        event_instance.ticket_ids.append(ticket_id)

        # publish the event
        publish_event_response = event_instance.publish_event(event_id=event_id)

        print("INFO: Successfully created and published the event to Eventbrite")
        return event_id

    def post_basic_info(self) -> dict:
        # TODO: check best way to modify the request's body
        url = f'{Eventbrite.BASE_URL}/organizations/{settings.EVENTBRITE_ORGANIZATION_ID}/events/'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
            'Accept': 'application/json',
        }

        end_datetime = self.start_datetime + timedelta(hours=self.duration)
        body = {
            "event": {
                "name": {
                    "html": self.title
                },
                "description": {
                    "html": self.description
                },
                "start": {
                    "timezone": self.start_datetime.tzname(),
                    "utc": self.start_datetime
                },
                "end": {
                    "timezone": end_datetime.tzname(),
                    "utc": end_datetime
                },
                "currency": self.currency,
                "online_event": self.is_online_event,
                "listed": self.is_listed,
                "shareable": self.is_shareable,
                "invite_only": self.is_invite_only,
                "show_remaining": self.show_remaining,
                "password": self.password,
                "capacity": self.seats
            }
        }

        response = requests.post(url=url, headers=headers, json=body)

        print("INFO: Successfully sent a post request to Eventbrite with event basic info")

        return response.json()

    def publish_event(self, event_id: str) -> dict:
        """
            Used to publish the event on eventbrite
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}/publish/'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
        }

        response = requests.post(url=url, headers=headers)

        print("INFO: Successfully sent a post request to Eventbrite to publish event.")

        return response.json()

    def delete_event(self, event_id: str) -> dict:
        """
            Not yet implemented.
            Can be used to delete the event specified by ${event_id}
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
        }

        response = requests.delete(url=url, headers=headers)

        print("INFO: Successfully deleted the event from Eventbrite")

        return response.json()

    def update_event(self, event_id: str, updated_body_field) -> dict:
        """
            Not yet implemented.
            This function will be used to update an event.
            Below is a working example of updating only the title of the event specified using ${event_id}
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}/'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
            'Accept': 'application/json',
        }

        body = {
            "event": {
                "name": {
                    "html": "Test Event Updated"
                }
            }
        }

        response = requests.post(url=url, headers=headers, json=body)

        print("INFO: Successfully updated event details on Eventbrite.")

        return response.json()


@dataclass()
class EventbriteTicket:
    """ required ticket fields to create an event ticket """
    # used to differentiate types of tickets such as Basic, VIP, etc
    type: str = ""
    # total number of tickets available for this ticket type
    quantity: int = 0
    # required only for free tickets
    is_free: bool = False
    # both below fields are required only for paid tickets
    cost: int = 0
    currency: str = ""

    @classmethod
    def create_ticket(cls, event_id: str, ticket_type: str, ticket_quantity: int, ticket_is_free: bool,
                      ticket_cost: int = 0, ticket_currency: str = "") -> str:
        """
            Initialize a free or paid ticket instance using the specified arguments
            then post the event ticket on Eventbrite
        """

        try:
            # create a paid ticket instance if ticket is not free
            if not ticket_is_free:
                # throw an error either the cost or currency is not specified for the paid ticket
                if ticket_cost <= 0 or not ticket_currency:
                    raise ValueError(
                        "400 (INVALID ARGUMENT ENTERED): Ticket is paid. Enter a valid cost value or valid currency."
                    )
                ticket_instance = cls(type=ticket_type, quantity=ticket_quantity, is_free=ticket_is_free,
                                      cost=ticket_cost, currency=ticket_currency)
            # else create a free ticket instance if ticket is free
            else:
                ticket_instance = cls(type=ticket_type, quantity=ticket_quantity, is_free=ticket_is_free)

        except ValueError as error:
            if not error:
                print("ERROR 400 (INVALID ARGUMENT ENTERED): Enter all required fields.", file=sys.stderr)
            else:
                print("ERROR", error, file=sys.stderr)
            return

        # send a post to eventbrite with the ticket details
        post_ticket_response = ticket_instance.post_ticket(event_id=event_id)

        # get the ticket id from the api response received
        ticket_id = post_ticket_response["id"]

        print("INFO: Successfully created the event ticket")

        return ticket_id

    def post_ticket(self, event_id: str) -> dict:
        """
            Send a post request to Eventbrite api to post the ticket information of the event
            specified by event_id
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}/ticket_classes/'

        headers = {
            'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}',
            'Accept': 'application/json',
        }

        body = {
            "ticket_class": {
                "name": self.type,
                "quantity_total": self.quantity,
                "free": self.free,
                "cost": f'{self.currency},{self.cost}'
            }
        }

        response = requests.post(url=url, headers=headers, json=body)

        print("INFO: Successfully sent a post request to Eventbrite with ticket info")

        return response.json()





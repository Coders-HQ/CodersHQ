from django.conf import settings
from datetime import datetime, timedelta, timezone
import requests
from dataclasses import dataclass, field
import sys
# import pytz

from eventbrite import Eventbrite


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


    @ classmethod
    def create_ticket(cls, event_id: str, ticket_type: str, ticket_quantity: int, ticket_is_free: bool,
                      ticket_currency: str, ticket_cost: int = 0) -> str:
        """
            Initialize a free or paid ticket instance using the specified arguments
            then post the event ticket on Eventbrite
        """

        try:
            # if ticket is paid, check if ticket cost value is greater than 0
            if not ticket_is_free and ticket_cost <= 0:
                # throw an error either the cost or currency is not specified for the paid ticket
                raise ValueError(
                    "400 (INVALID ARGUMENT ENTERED): Ticket is paid. Enter a cost value greater than 0"
                )
            
            # create a ticket instance
            ticket_instance = cls(type=ticket_type, quantity=ticket_quantity, is_free=ticket_is_free, 
                                  cost=ticket_cost, currency=ticket_currency)

        except ValueError as error:
            if not error:
                print("ERROR 400 (INVALID ARGUMENT ENTERED): Enter all required fields of a ticket.", file=sys.stderr)
            else:
                print("ERROR", error, file=sys.stderr)
            return ""

        # send a post request to Eventbrite with the ticket details
        post_ticket_response = ticket_instance.post_ticket(event_id=event_id)

        # display an error if process of creating a ticket failed
        if not post_ticket_response:
            print("WARNING: Failed to create ticket - Event is partially created on Eventbrite and will not work properly")

            del ticket_instance
            print("INFO: Successfully deleted ticket instance created in system")

            return ""

        # get the ticket id from the post response received
        ticket_id = post_ticket_response["id"]

        print("INFO: Successfully created the event ticket")

        return ticket_id


    def post_ticket(self, event_id: str) -> dict:
        """
            Send a post request to Eventbrite api to post the ticket information of the event
            specified by event_id
        """

        url = f'{Eventbrite.BASE_URL}/events/{event_id}/ticket_classes/'

        ticket_body = {
            "ticket_class": {
                "name": self.type,
                "quantity_total": self.quantity,
                "free": self.is_free,
                "cost": f'{self.currency},{self.cost}'
            }
        }

        # send ticket details to eventbrite api
        response = Eventbrite.post_request(url=url, body=ticket_body)

        # display an error if sending ticket details to eventbrite api failed
        if not response:
            print("ERROR: Failed to post ticket details on Eventbrite")
            return {}

        print("INFO: Successfully sent a post request with ticket details")

        return response
'''Controller related to trips_repository.py and emails_repository.py'''
from typing import Dict
import uuid
from src.drivers.email_sender import send_email


class TripCreatorController:
    '''Service for creating trips and associated email invitations.

    Attributes:
        __trip_repository: Repository for managing trip data.
        __email_repository: Repository for managing email invitation data.
    '''

    def __init__(self, trips_repository, emails_repository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        '''Creates a new trip and associated email invitations.

        Args:
            body: A dictionary containing the trip information and optionally emails to invite.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the trip ID and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id}

            self.__trips_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
            send_email([body["owner_email"]],
                       f"http://localhost:3000/trips/{trip_id}/confirm")

            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

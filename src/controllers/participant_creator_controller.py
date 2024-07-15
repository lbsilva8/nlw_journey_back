'''Controller related to participants_repository.py and email_to_invite_repository.py'''
from typing import Dict
import uuid


class ParticipantCreatorController:
    '''Controller for handling the creation of participants associated with trips.

    Attributes:
        __participants_repository: Repository for managing participant data.
        __email_repository: Repository for managing email data
    '''

    def __init__(self, participants_repository, emails_repository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, trip_id) -> Dict:
        '''Creates a new participant and associated email for a specific trip.

        Args:
            body (Dict): A dictionary containing participant and email information.
            trip_id (str): The ID of the trip to associate the participant with.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the participant ID and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {**body, "id": email_id, "trip_id": trip_id}
            participants_infos = {**body, "id": participant_id,
                                  "trip_id": trip_id, "emails_to_invite_id": email_id}

            self.__emails_repository.registry_email(emails_infos)
            self.__participants_repository.registry_participants(
                participants_infos)

            return {
                "body": {"participant_id": participant_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

'''Controller related to participants_repository.py'''
from typing import Dict


class ParticipantFinderController:
    '''Controller for handling the retrieval of participants associated with trips.

    Attributes:
        __participant_repository: Repository for managing participant data.
    '''

    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository

    def find(self, trip_id) -> Dict:
        '''Retrieves all participants for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve participants for.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains a list of participants and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            participants = self.__participants_repository.find_participants_from_trip(
                trip_id)

            participants_infos = []
            for participant in participants:
                participants_infos.append({
                    "id": participant[0],
                    "name": participant[1],
                    "is_confirm": participant[2],
                    "email": participant[3],
                })

            return {
                "body": {"participants": participants_infos},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

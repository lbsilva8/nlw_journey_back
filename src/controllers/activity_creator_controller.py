'''Controller related to activities_repository.py'''
from typing import Dict
import uuid


class ActivityCreatorController:
    '''Controller for handling the creation of activities associated with trips.

    Attributes:
        __activities_repository: Repository for managing activity data.
    '''

    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, trip_id) -> Dict:
        '''Creates a new activity for a specific trip.

        Args:
            body (Dict): A dictionary containing activity information.
            trip_id (str): The ID of the trip to associate the activity with.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the activity ID and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''

        try:
            id = str(uuid.uuid4())
            activities_infos = {**body, "id": id, "trip_id": trip_id}

            self.__activities_repository.registry_activity(
                activities_infos)

            return {
                "body": {"pactivity_id": id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

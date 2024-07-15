'''Controller related to activitie_repository.py'''
from typing import Dict


class ActivityFinderController:
    '''Controller for handling the retrieval of activities associated with trips.

    Attributes:
        __activities_repository: Repository for managing activity data.
    '''

    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find(self, trip_id) -> Dict:
        '''Retrieves all activities for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve activities for.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains a list of activities and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            activities = self.__activities_repository.find_activities_from_trip(
                trip_id)

            activities_infos = []
            for activity in activities:
                activities_infos.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3],
                })

            return {
                "body": {"participants": activities_infos},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

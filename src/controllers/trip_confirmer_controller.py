'''Controller related to trip_repository.py'''
from typing import Dict


class TripConfirmerController:
    '''Controller for handling the confirmation of trips.

    Attributes:
        __trip_repository: Repository for managing trip data.
    '''

    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def confirm(self, trip_id) -> Dict:
        '''Confirms a trip by updating its status.

        Args:
            trip_id (str): The ID of the trip to confirm.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body is None and the status code is 204.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {
                "body": None,
                "status_code": 204
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

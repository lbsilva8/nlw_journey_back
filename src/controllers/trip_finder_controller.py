'''Controller related to trip_repository.py'''
from typing import Dict


class TripFinderController:
    '''Controller for handling the retrieval of trip details.

    Attributes:
        __trip_repository: Repository for managing trip data.
    '''

    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def find(self, trip_id) -> Dict:
        '''Finds the details of a specific trip by its ID.

        Args:
            trip_id (str): The ID of the trip to retrieve.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the trip details and a 200 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No Trip Found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "start_date": trip[2],
                        "end_date": trip[3],
                        "status": trip[6]
                    }
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

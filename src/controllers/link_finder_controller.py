'''Controller related to link_repository.py'''
from typing import Dict


class LinkFinderController:
    '''Controller for handling the retrieval of links associated with trips.

    Attributes:
        __link_repository: Repository for managing link data.
    '''

    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def find(self, trip_id) -> Dict:
        '''Finds all links associated with a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve links for.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the list of links and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            links = self.__link_repository.find_links_from_trip(trip_id)

            formatted_links = []
            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "link": link[2],
                    "title": link[3],
                })

            return {
                "body": {"links": formatted_links},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

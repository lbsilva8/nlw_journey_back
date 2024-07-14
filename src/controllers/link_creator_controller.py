'''Controller related to link_repository.py'''
from typing import Dict
import uuid


class LinkCreatorController:
    '''Controller for handling the creation of links associated with trips.

    Attributes:
        __link_repository: Repository for managing link data.
    '''

    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id) -> Dict:
        '''Creates a new link associated with a specific trip.

        Args:
            body (Dict): A dictionary containing link information.
            trip_id (str): The ID of the trip to associate the link with.

        Returns:
            Dict: A dictionary with the response body and status code.
                On success, the body contains the link ID and a 201 status code.
                On failure, the body contains an error message and a 400 status code.
        '''
        try:
            link_id = str(uuid.uuid4())
            link_infos = {**body, "id": link_id, "trip_id": trip_id}

            self.__link_repository.registry_link(link_infos)
            return {
                "body": {"linkId": link_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

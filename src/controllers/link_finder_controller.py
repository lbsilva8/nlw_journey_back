'''Controller related to link_repository.py'''
from typing import Dict


class LinkFinderController:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def find(self, trip_id) -> Dict:
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

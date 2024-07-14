'''Interaction with database activities table'''
from sqlite3 import Connection
from typing import Dict, Tuple, List


class ActivitiesRepository:
    '''Repository for managing activities related to trips in the database.

    Attributes:
        __conn (sqlite3.Connection): The database connection object.
    '''

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activitie(self, activities_infos: Dict) -> None:
        '''Inserts a new activity into the activities table.

        Args:
            activities_infos (Dict): A dictionary containing activity information.
                Expected keys: "id", "trip_id", "title", "occurs_at".
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO activities
                (id, trip_id , title, occurs_at)
            VALUES
                (?, ?, ?, ?)
            ''',  (
                activities_infos["id"],
                activities_infos["trip_id"],
                activities_infos["title"],
                activities_infos["occurs_at"]
            )
        )
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        '''Retrieves all activities for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve activities for.

        Returns:
            List[Tuple]: A list of tuples containing activity details.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM activities WHERE trip_id = ?''', (trip_id,)
        )
        activities = cursor.fetchall()
        return activities

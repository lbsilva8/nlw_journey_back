'''Interaction with database trips table'''
from sqlite3 import Connection
from typing import Dict, Tuple


class TripsRepository:
    '''Repository for managing trip data in the database.

    Attributes:
        __conn (sqlite3.Connection): The database connection object.
    '''

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trips_infos: Dict) -> None:
        '''Inserts a new trip into the trips table.

        Args:
            trips_infos (Dict): A dictionary containing trip information.
            Expected keys: "id", "destination", "star_date", "end_date", "owner_name", "owner_email".
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO trips
                (id, destination, star_date, end_date, owner_name, owner_email)
            VALUES
                (?, ?, ?, ?, ?, ?)
            ''',  (
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["star_date"],
                trips_infos["end_date"],
                trips_infos["owner_name"],
                trips_infos["owner_email"]
            )
        )
        self.__conn.commit()

    def find_trip_by_id(self, trip_id: str) -> Tuple:
        '''Retrieves a trip from the trips table by its ID.

        Args:
            trip_id (str): The ID of the trip to retrieve.
        Returns:
            Tuple: The trip information as a tuple. Returns None if no trip is found.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM trips WHERE id = ?''', (trip_id,)
        )
        trip = cursor.fetchone()
        return trip

    def update_trip_status(self, trip_id: str) -> None:
        '''Updates the status of a trip to 1 (completed).

        Args:
            trip_id (str): The ID of the trip to update.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE trips
                    SET status = 1
                WHERE
                    id = ?
            ''', (trip_id,)
        )
        self.__conn.commit()

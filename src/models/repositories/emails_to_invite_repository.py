'''Interaction with database emails_to_invite table'''
from sqlite3 import Connection
from typing import Dict, Tuple, List


class EmailsToInviteRepository:
    '''Repository for managing email invitations related to trips in the database.

    Attributes:
        __conn (sqlite3.Connection): The database connection object.
    '''

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, email_infos: Dict) -> None:
        '''Inserts a new email invitation into the emails_to_invite table.

        Args:
            email_infos (Dict): A dictionary containing email invitation information.
                Expected keys: "id", "trip_id", "email".
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO emails_to_invite
                (id, trip_id , email)
            VALUES
                (?, ?, ?)
            ''',  (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"]
            )
        )
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        '''Retrieves all email invitations for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve email invitations for.
        Returns:
            List[Tuple]: A list of tuples containing the email invitations.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE trip_id = ?''', (trip_id,)
        )
        trip = cursor.fetchall()
        return trip

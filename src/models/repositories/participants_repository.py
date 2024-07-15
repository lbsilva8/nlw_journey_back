'''Interaction with database participants table'''
from sqlite3 import Connection
from typing import Dict, Tuple, List


class ParticipantsRepository:
    '''Repository for managing participants related to trips in the database.

    Attributes:
        __conn (sqlite3.Connection): The database connection object.
    '''

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participants(self, participants_infos: Dict) -> None:
        '''Inserts a new participant into the participants table.

        Args:
            participants_infos (Dict): A dictionary containing participant information.
                Expected keys: "id", "trip_id", "email_to_invite_id", "name".
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO participants
                (id, trip_id, emails_to_invite_id, name)
            VALUES
                (?, ?, ?, ?)
            ''',  (
                participants_infos["id"],
                participants_infos["trip_id"],
                participants_infos["emails_to_invite_id"],
                participants_infos["name"]
            )
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        '''Retrieves all participants for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve participants for.

        Returns:
            List[Tuple]: A list of tuples containing participant details.

        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                FROM participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants

    def update_participants_status(self, participants_id: str) -> None:
        '''Updates the status of a participant to confirmed.

        Args:
            participants_id (str): The ID of the participant to update.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                SET is_confirmed = 1
                WHERE id = ?
            ''', (participants_id,)
        )
        self.__conn.commit()

'''Interaction with database links table'''
from sqlite3 import Connection
from typing import Dict, Tuple, List


class LinksRepository:
    '''Repository for managing links related to trips in the database.

    Attributes:
        __conn (sqlite3.Connection): The database connection object.
    '''

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_infos: Dict) -> None:
        ''' Inserts a new link into the links table.

        Args:
            link_infos (Dict): A dictionary containing link information.
                Expected keys: "id", "trip_id", "link", "title".
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links
                (id, trip_id , link, title)
            VALUES
                (?, ?, ?, ?)
            ''',  (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"]
            )
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        '''Retrieves all links for a specific trip.

        Args:
            trip_id (str): The ID of the trip to retrieve links for.

        Returns:
            List[Tuple]: A list of tuples containing the links.
        '''
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        links = cursor.fetchall()
        return links

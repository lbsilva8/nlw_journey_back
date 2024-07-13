'''Tests related to links_repository.py'''

import pytest
import uuid
from src.models.settings.db_conection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interaction with the database")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    links_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "link.com",
        "title": "Hotel"
    }
    link_repository.registry_link(links_infos)


@pytest.mark.skip(reason="interaction with the database")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    response = link_repository.find_links_from_trip(trip_id)
    assert isinstance(response, list)
    assert isinstance(response[0], tuple)

'''Tests related to trips_repository.py'''
import uuid
import pytest
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_conection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interaction with the database")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "star_date": datetime.strptime("02-01-2021", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2021", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }

    trips_repository.create_trip(trips_infos)


@pytest.mark.skip(reason="interaction with the database")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)


@pytest.mark.skip(reason="interaction with the database")
def test_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)

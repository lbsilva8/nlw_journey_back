'''Routes to be accessed by user'''
from src.models.settings.db_conection_handler import db_connection_handler
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.controllers.trip_creator_controller import TripCreatorController
from src.controllers.trip_finder_controller import TripFinderController
from src.controllers.link_creator_controller import LinkCreatorController
from src.controllers.trip_confirmer_controller import TripConfirmerController
from flask import jsonify, Blueprint, request
trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    '''Endpoint to create a new trip.

    This function handles the POST request to create a new trip.
    It is currently a placeholder that returns a simple JSON response indicating that a trip was created.

    Returns:
        Response: A JSON response with the body and status code.
    '''
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreatorController(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip(trip_id):
    '''Endpoint to find details of a specific trip by its ID.

    This function handles the GET request to retrieve the details of a trip.
    It uses the TripFinderController to fetch the trip details from the database.

    Args:
        tripId (str): The ID of the trip to retrieve.

    Returns:
        Response: A JSON response with the trip details and the status code.
    '''
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinderController(trips_repository)

    response = controller.find_trip_details(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
    '''Endpoint to confirm a trip by updating its status.

    This function handles the GET request to confirm a trip. It uses the 
    TripConfirmerController to update the trip status in the database.

    Args:
        trip_id (str): The ID of the trip to confirm.

    Returns:
        Response: A JSON response with the confirmation result and the status code.
    '''

    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmerController(trips_repository)

    response = controller.confirm(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["POST"])
def create_trip_link(trip_id):
    '''Endpoint to create a link associated with a specific trip.

    This function handles the POST request to create a new link for a trip.
    It uses the LinkCreatorController to add the link to the database.

    Args:
        trip_id (str): The ID of the trip to associate the link with.

    Returns:
        Response: A JSON response with the creation result and the status code.
    '''

    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreatorController(links_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]

'''Routes to be accessed by user'''
# imports conections
from src.models.settings.db_conection_handler import db_connection_handler

# imports from repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

# imports from controllers
from src.controllers.trip_creator_controller import TripCreatorController
from src.controllers.trip_finder_controller import TripFinderController
from src.controllers.trip_confirmer_controller import TripConfirmerController

from src.controllers.link_creator_controller import LinkCreatorController
from src.controllers.link_finder_controller import LinkFinderController

from src.controllers.activity_creator_controller import ActivityCreatorController
from src.controllers.activity_finder_controller import ActivityFinderController

from src.controllers.participant_creator_controller import ParticipantCreatorController
from src.controllers.participant_confirmer_controller import ParticipantConfirmerController
from src.controllers.participant_finder_controller import ParticipantFinderController

# other imports
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

    response = controller.find(trip_id)

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


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
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


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["GET"])
def find_trip_link(trip_id):
    ''' Endpoint to find all links associated with a specific trip.

    This function handles the GET request to retrieve all links for a trip.
    It uses the LinkFinderController to fetch the links from the database.

    Args:
        trip_id (str): The ID of the trip to retrieve links for.

    Returns:
        Response: A JSON response with the links and the status code.
    '''

    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinderController(links_repository)

    response = controller.find(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/invites", methods=["POST"])
def invite_to_trip(trip_id):
    '''Endpoint to invite participants to a specific trip.

    This function handles the POST request to invite participants to a trip.
    It uses the ParticipantCreatorController to create participants and
    associated emails in the database.

    Args:
        trip_id (str): The ID of the trip to invite participants to.

    Returns:
        Response: A JSON response with the participant ID and the status code.
            On success, the response body contains the participant ID and a 201 status code.
            On failure, the response body contains an error message and a 400 status code.
    '''

    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreatorController(
        participants_repository, email_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/activities", methods=["POST"])
def create_activity(trip_id):
    '''Endpoint to create an activity for a specific trip.

    This function handles the POST request to create an activity for a trip.
    It uses the ActivityCreatorController to register the activity in the database.

    Args:
        trip_id (str): The ID of the trip to associate the activity with.

    Returns:
        Response: A JSON response with the activity ID and the status code.
            On success, the response body contains the activity ID and a 201 status code.
            On failure, the response body contains an error message and a 400 status code.
    '''

    conn = db_connection_handler.get_connection()
    activites_repository = ActivitiesRepository(conn)
    controller = ActivityCreatorController(activites_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/activities", methods=["GET"])
def find_activity(trip_id):
    '''Endpoint to retrieve activities for a specific trip.

    This function handles the GET request to retrieve activities associated with a trip.
    It uses the ActivityFinderController to fetch the activities from the database.

    Args:
        trip_id (str): The ID of the trip to retrieve activities for.

    Returns:
        Response: A JSON response with the list of activities and the status code.
            On success, the response body contains the list of activities and a 201 status code.
            On failure, the response body contains an error message and a 400 status code.
    '''

    conn = db_connection_handler.get_connection()
    activites_repository = ActivitiesRepository(conn)
    controller = ActivityFinderController(activites_repository)

    response = controller.find(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/invites", methods=["GET"])
def find_participants_from_trip(trip_id):
    '''Endpoint to retrieve participants for a specific trip.

    This function handles the GET request to retrieve participants associated with a trip.
    It uses the ParticipantFinderController to fetch the participants from the database.

    Args:
        trip_id (str): The ID of the trip to retrieve participants for.

    Returns:
        Response: A JSON response with the list of participants and the status code.
            On success, the response body contains the list of participants and a 201 status code.
            On failure, the response body contains an error message and a 400 status code.
    '''

    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinderController(participants_repository)

    response = controller.find(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<participant_id>/confirm", methods=["PATCH"])
def confirm_participants_to_invite(participant_id):
    '''Endpoint to confirm a participant's invitation to a trip.

    This function handles the PATCH request to confirm a participant's invitation.
    It uses the ParticipantConfirmerController to update the participant's status in the database.

    Args:
        participant_id (str): The ID of the participant to confirm.

    Returns:
        Response: A JSON response with the status code.
            On success, the response body is None and the status code is 204.
            On failure, the response body contains an error message and a 400 status code.s
    '''

    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmerController(participants_repository)

    response = controller.confirm(participant_id)

    return jsonify(response["body"]), response["status_code"]

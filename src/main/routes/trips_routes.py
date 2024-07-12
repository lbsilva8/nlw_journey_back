'''Routes to be accessed by user'''
from flask import jsonify, Blueprint

trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    '''Endpoint to create a new trip.

    This function handles the POST request to create a new trip. 
    It is currently a placeholder that returns a simple JSON response indicating that a trip was created.

    Returns:
        Response: A JSON response with the trip status.
    '''
    return jsonify({"trip": "create"})

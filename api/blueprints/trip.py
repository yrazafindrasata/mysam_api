from flask import Blueprint, jsonify, request

from api.model import Trip , Client, Driver
from api.database import db


trip = Blueprint('trip', __name__, url_prefix='/trip')


@trip.route("/accept", methods=['PATCH'])
def accept_trip():
    try:
        trip_id = request.args.get("tripId")
        driver_id = request.args.get("driverId")
        update_state = Trip.query.get(trip_id).update({"id_state": 1, "id_driver": driver_id})
        db.session.commit()

    except Exception as err:
        db.session.rollback()
        message = {"status": "ERROR", "status_code": 400, "message": "{}".format(err)}
        resp = jsonify(message)
        resp.status_code = 400
        return resp
    else:
        return jsonify(status="OK", status_code=200, message='Item id={} successfully updated.'.format(trip_id))


@trip.route("/start", methods=['PATCH'])
def start_trip():
    try:
        trip_id = request.args.get("tripId")
        update_state = Trip.query.get(trip_id).update({"id_state": 2})
        db.session.commit()

    except Exception as err:
        db.session.rollback()
        message = {"status": "ERROR", "status_code": 400, "message": "{}".format(err)}
        resp = jsonify(message)
        resp.status_code = 400
        return resp
    else:
        return jsonify(status="OK", status_code=200, message='Item id={} successfully updated.'.format(trip_id))


@trip.route("/end", methods=['PATCH'])
def end_trip():
    try:
        trip_id = request.args.get("tripId")
        update_trip = trip_object.update({"id_state": 3})

        current_trip = Trip.query.get(trip_id)
        total_coast = 1.40 * trip_object.distance

        current_client = Client.query.get(current_trip.id_client)
        new_balance_client = client_current.balance - total_coast
        current_client.update({"balance": new_balance_client})

        current_driver = Driver.query.get(current_trip.id_driver)
        new_balance_driver = driver_current.balance + total_coast * 85/100
        current_driver.update({"balance": new_balance_driver})

        db.session.commit()

    except Exception as err:
        db.session.rollback()
        message = {"status": "ERROR", "status_code": 400, "message": "{}".format(err)}
        resp = jsonify(message)
        resp.status_code = 400
        return resp
    else:
        return jsonify(status="OK", status_code=200, message='Item id={} successfully updated.'.format(trip_id))



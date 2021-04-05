from flask import Blueprint, jsonify, request
from src.dbconn import get_db_connection


simple_page_3 = Blueprint('simple_page_3', __name__, template_folder='templates')


@simple_page_3.route('/vaccination_centre', methods = ["GET", "POST"])
def vaccination_centre():
    if request.method == "GET":
        connection=get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select * from Vaccination_Centre")
            response = jsonify(cursor.fetchall())
        except Exception as e:
            response = jsonify({"status": "failure"})
            print(e)
        cursor.close()
        connection.close()
        return response

    if request.method == 'POST':
        connection=get_db_connection()
        address = request.form['address']
        dose_count = request.form['dose_count']
        dose_type_ID = request.form['dose_type_ID']
        cursor = connection.cursor()
        try:
            cursor.execute("insert into Vaccination_Centre (address, dose_count, dose_type_ID) values (%s, %s, %s)",(address, dose_count, dose_type_ID))
            connection.commit()
            response = jsonify({"status": "success"})
        except Exception as e:
            response = jsonify({"status":"failure"})
            print(e)
        cursor.close()
        connection.close()
        return response


@simple_page_3.route('/vaccination_centre/<string:address>')
def get_vaccination_centre_address(address):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Vaccination_Centre where Vaccination_Centre.address = %s ",(address,))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response


@simple_page_3.route('/vaccination_centre/<int:id>')
def get_vaccination_centre_id(id):
    connection=get_db_connection()
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute("select * from Vaccination_Centre where Vaccination_Centre.ID = %s ", (int(id),))
        response = jsonify(cursor.fetchall())
    except Exception as e:
        response = jsonify({"status": "failure"})
        print(e)
    cursor.close()
    connection.close()
    return response
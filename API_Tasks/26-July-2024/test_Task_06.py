# 4. Create a BOOKING, Delete It.

import json
import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests


def create_token():
    # token
    Url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=Url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


def test_create_booking():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    return booking_id


def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    booking_id = test_create_booking()
    DELETE_URL = URL + str(booking_id)

    cookie_value = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    print(response.status_code == 200)

import pytest
import json
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"


@pytest.fixture()
def create_token():
    url = base_url + "/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()['token']
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    url = base_url + "/booking"

    headers = {'Content-Type': 'application/json'}

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    post_response = requests.post(url=url, headers=headers, json=payload)
    print(post_response.status_code)
    data = post_response.json()
    booking_id = data['bookingid']
    return booking_id


def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)


def test_update_req_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

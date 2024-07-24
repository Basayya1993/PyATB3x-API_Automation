import json
import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"


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


def create_booking():
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


@allure.title("Automation Testing PUT API Test Case")
@allure.description("Verify Automation PUT Request")
@pytest.mark.put_request
def test_put_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    put_url = base_url + base_path
    cookie = "token=" + create_token()

    headers = {
        'Content-Type': 'application/json',
        'Cookie': cookie
    }

    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    put_response = requests.put(url=put_url, headers=headers, json=payload)
    print(put_response.status_code)
    assert put_response.status_code == 200

    data = put_response.json()
    print(data)
    assert data["firstname"] == "James"

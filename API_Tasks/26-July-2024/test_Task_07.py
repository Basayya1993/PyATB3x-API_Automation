# 5. Invalid Creation - Enter a wrong payload or Wrong JSON.

import json
import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests


def test_create_booking():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(json_payload)

    # Assertions
    assert response.status_code == 500
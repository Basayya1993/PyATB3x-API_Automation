# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and
# Verify using GET by id.
import json

import allure  # pip install allure
import pytest  # pip install pytest
import requests  # pip install requests

base_url = "https://restful-booker.herokuapp.com"


def test_get_request():
    base_path = "/booking/71"
    GET_URL = base_url + base_path

    get_request = requests.get(url=GET_URL)

    json_data = get_request.json()
    print(json_data)












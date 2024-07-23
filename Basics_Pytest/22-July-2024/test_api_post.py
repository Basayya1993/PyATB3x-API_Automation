import json
import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"


@allure.title("Automation Testing Get API Test Case")
@allure.description("Verify Automation Get Request")
@pytest.mark.get_request
def test_get_positive():
    url = base_url + "/booking/1"

    get_response = requests.get(url=url)
    print(get_response.status_code)
    assert get_response.status_code == 200

    json_data = get_response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON String:", json_str)
    json_id = json.loads(json_str)
    user_id = json_id['firstname']
    print(user_id)


@allure.title("Automation Testing POST API Test Case")
@allure.description("Verify Automation POST Request")
@pytest.mark.post_request
def test_post_positive():
    url = base_url + "/booking"

    headers = {
        'content-type': 'application/json'
    }

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
    assert post_response.status_code == 200

    json_data = post_response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON String:", json_str)
    json_id = json.loads(json_str)
    user_id = json_id['bookingid']
    print(user_id)

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

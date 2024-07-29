# API Testing - Automation Home.
# Integration Scenarios
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404

# Test for the Single Req
# 1. Response
# 2. Status Code
# 3. Headers -----> Assertions will always (negative)

import pytest


@pytest.fixture()
def sample_data():
    data = [1, 2, 3, 4, 5]  # type - list
    return data


@pytest.fixture()
def sample_data2():
    return True


def test_consume_sample_1_2(sample_data, sample_data2):
    print(sample_data)
    print(sample_data2)

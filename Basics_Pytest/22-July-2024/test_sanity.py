import pytest
import allure


@allure.title("Test Case #1 Addition")
@allure.description("Verify the Positive Test Case")
@allure.tag("TestCase#1")
@pytest.mark.sanity
def test_addition():
    assert 4 + 1 == 5, "Test Case Pass"


@allure.title("Test Case #2 Subtraction")
@allure.description("Verify the Negative Test Case")
@allure.tag("TestCase#2")
@pytest.mark.sanity
def test_sub():
    assert 4 - 1 == 2, "Test Case Fail"


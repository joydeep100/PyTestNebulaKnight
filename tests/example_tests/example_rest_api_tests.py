import requests
import pytest
import logging
from utils.get_env_details import get_env_details
from assertpy import assert_that

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

# since headers are common defining here
# TODO :: Pick token from --secret command line arg
headers = {
    'Authorization': 'Bearer sampleToken',
    'Content-Type': 'application/json'
}


@pytest.fixture(scope="module")
def shared_data():
    '''using this fixture to share data across tests'''
    data = {}
    yield data


@pytest.fixture(scope="module")
def global_setup(request):
    '''context will contain all env variables & env specific data stored in configs/env_data'''
    context = get_env_details(request)
    yield context

@pytest.mark.smoke
def test_create_user_api(global_setup, shared_data):
    url = global_setup['apiurl'] + "api/users"
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url, headers=headers, json=body)
    assert_that(response.status_code).is_equal_to(201)

    response_data = response.json()
    assert_that(response_data["name"]).is_equal_to("morpheus")
    assert_that(response_data["job"]).is_equal_to("leader")
    assert_that(response_data).contains_key("id")

    # example of sharing data across tests, here we are storing 'id' in shared_data
    shared_data['id'] = response_data["id"]

@pytest.mark.regression
def test_update_user_api(global_setup, shared_data):

    url = global_setup['apiurl'] + "api/users/2"

    id = shared_data.get('id')
    # getting value of id from shared_data
    body = {
        "name": "morpheus updated",
        "job": "leader",
        "id": id  # using shared_data
    }
    response = requests.put(url, headers=headers, json=body)
    assert_that(response.status_code).is_equal_to(200)

    response_data = response.json()
    assert_that(response_data["name"]).is_equal_to("morpheus updated")
    assert_that(response_data["id"]).is_equal_to(id)  # using shared_data


def test_get_user_api(global_setup, shared_data):
    url = global_setup['apiurl'] + "api/users/2"

    response = requests.get(url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

    response_data = response.json()
    assert_that(response_data["data"]["id"]).is_equal_to(2)


@pytest.mark.skip(reason="no way of currently testing this")
def dummy_test(global_setup, shared_data):
    logger.info('Hey i am just fooling around!')

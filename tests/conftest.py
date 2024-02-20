import pytest
from webshotapi import Client
import os


@pytest.fixture
def request_client() -> Client:
    return Client(os.environ['WEBSHOTAPI_TEST_API_KEY'], "v1", os.environ['WEBSHOTAPI_ENDPOINT'])

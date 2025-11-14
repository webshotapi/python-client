import pytest
from webshotapi import Client
import os


@pytest.fixture
def request_client() -> Client:
    return Client(os.environ['WEBSHOTAPI_KEY'], api_host=os.environ['WEBSHOTAPI_ENDPOINT'])

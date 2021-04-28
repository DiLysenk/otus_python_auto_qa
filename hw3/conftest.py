import requests
import pytest

@pytest.fixture
def response_get(end_point):
    return requests.get(end_point)  # response содержит уже все хедеры и тд
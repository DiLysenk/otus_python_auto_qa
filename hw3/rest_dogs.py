from urllib import response

import requests
import pytest


di
@pytest.fixture
def get_api(end_point):
    return requests.get(end_point) # response содержит уже все хедеры и тд



@pytest.mark.parametrize("end_point",['https://dog.ceo/api/breeds/list/all',
                                      'https://dog.ceo/api/breeds/image/random',
                                      'https://dog.ceo/api/breed/hound/images',
                                      'https://dog.ceo/api/breed/hound/list',
                                      'https://dog.ceo/api/breed/boxer/images/random'])
def test_dog_api(get_api, end_point):
    assert get_api.status_code == 200
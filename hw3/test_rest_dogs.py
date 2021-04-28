import pytest
from jsonschema import validate


@pytest.mark.parametrize("end_point", ['https://dog.ceo/api/breeds/list/all',
                                       'https://dog.ceo/api/breeds/image/random',
                                       'https://dog.ceo/api/breed/hound/images',
                                       'https://dog.ceo/api/breed/hound/list',
                                       'https://dog.ceo/api/breed/boxer/images/random'])
def test_dog_api_status(response_get, end_point):
    assert response_get.status_code == 200


@pytest.mark.parametrize("end_point", ['https://dog.ceo/api/breeds/list/all'])
def test_dog_api_schema(response_get, end_point):
    schema = {
        "type": "object",
        'properties': {
            'massage': {"type": "object"}
        }

    }


    validate(instance=response_get.json(), schema=schema)


# def test_dog_api_json(response_get):
#     assert response_get.contetnt == "content"

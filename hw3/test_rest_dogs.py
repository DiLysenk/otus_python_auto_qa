import pytest
from jsonschema import validate
import cerberus


@pytest.mark.parametrize("end_point", ['https://dog.ceo/api/breeds/list/all',
                                       'https://dog.ceo/api/breeds/image/random',
                                       'https://dog.ceo/api/breed/hound/images',
                                       'https://dog.ceo/api/breed/hound/list',
                                       'https://dog.ceo/api/breed/boxer/images/random'])
def test_dog_api_status(response_get, end_point):
    assert response_get.status_code == 200


# Валидация схемы
@pytest.mark.parametrize("end_point", ['https://dog.ceo/api/breeds/list/all'])
def test_dog_api_schema(response_get, end_point):
    schema = {
        "type": "object",
        'properties': {
            'message': {"type": "object"}
        }
    }
    # validate возвращает None поэту assert не используем
    validate(instance=response_get.json(), schema=schema)


# Валидация схемы с помощью cerberus
@pytest.mark.parametrize("end_point", ['https://dog.ceo/api/breeds/list/all'])
def test_dog_api_schema_cerebrus(response_get, end_point):
    schema_c = {
        'message': {'type': 'dict'},
        'status': {'type': 'string', } # валидация стринги статус, отделить схему от теста
    }
    v = cerberus.Validator()
    assert v.validate(response_get.json(), schema_c)


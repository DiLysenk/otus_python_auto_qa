import cerberus
import pytest
from jsonschema import validate


# проверка 200
def test_api_status(response_get):
    assert response_get.status_code == 200


# проверка статуса "success"
def test_api_include_id(response_get):
    assert 1 == response_get.json()[0].get('id')


# Валидация части схемы jsonschema validate
@pytest.mark.parametrize("end_point", ['https://jsonplaceholder.typicode.com/posts'])
def test_api_schema(response_get, end_point):
    schema = {
        "type": "object",  # ожидаем что придёт dict
        'properties': {  # с атрибутами message status
            'user': {"type": "integer"},
            'id': {"type": "integer"},
            'title': {"type": "string"},
            'body': {"type": "string"},
        },
        'required': ['id'],  # обязательные поля
        'maxProperties': 4  # максимальное количество
    }
    # validate возвращает None поэту assert не используем
    validate(instance=response_get.json()[0], schema=schema)


# Валидация части схемы с помощью cerberus
@pytest.mark.parametrize("end_point", ['https://jsonplaceholder.typicode.com/comments'])
@pytest.mark.parametrize("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_api_schema_cerebrus(response_get, end_point, i):
    schema = {
        'postId': {"type": "integer"},
        'id': {"type": "integer"},
        'name': {"type": "string"},
        'email': {"type": "string", 'regex': "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
        'body': {"type": "string"},  # валидация стринги статус, отделить схему от теста
    }
    v = cerberus.Validator()
    assert v.validate(response_get.json()[i], schema)


# валидация части схемы с помощью
@pytest.mark.parametrize("end_point", ['https://jsonplaceholder.typicode.com/albums'])
def test_api_albums(response_get, end_point):
    schema = {
        'userId': {'type': 'integer'},
        'id': {'type': 'integer'},
        'title': {'type': 'string'}
    }
    v = cerberus.Validator()
    assert v.validate(response_get.json()[0], schema)

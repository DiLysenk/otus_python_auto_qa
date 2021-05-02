import cerberus
import pytest
from deepdiff import DeepDiff
from jsonschema import validate

v = cerberus.Validator()

# проверка 200
def test_brewery_api_status(response_get):
    assert response_get.status_code == 200


# Валидация части схемы jsonschema validate
@pytest.mark.parametrize("end_point", ['https://api.openbrewerydb.org/breweries/9094'])
def test_brewery_api_schema(response_get, end_point):
    value = {"anyOf": [{"type": "string"}, {"type": "null"}]}
    schema = {
        "type": "object",  # ожидаем что придёт dict
        'properties': {  # с атрибутами  status
            'id': {"type": "integer"},
            'obdb_id': value,
            'name': {"type": "string"},
            'brewery_type': value,
            'street': value,
            'address_2': value,
            'address_3': value,
            'city': value,
            'county_province': value,
            'state': value,
            'postal_code': value,
            'country': value,
            'longitude': value,
            'latitude': value,
            'phone': value,
            'website_url': value,
            'updated_at': value,
            'created_at': value
        }
    }
    # validate возвращает None поэтому assert не используем
    validate(instance=response_get.json(), schema=schema)


# Валидация части схемы с помощью cerberus
@pytest.mark.parametrize("end_point", ['https://api.openbrewerydb.org/breweries/9094'])
def test_brewery_api_schema_cerebrus(response_get, end_point):
    value = {"type": 'string', 'nullable': True}
    schema = {
        'id': {"type": "integer"},
        'name': {'type': 'string'},
        'obdb_id': value,
        'brewery_type': value,
        'street': value,
        'address_2': value,
        'address_3': value,
        'city': value,
        'county_province': value,
        'state': value,
        'postal_code': value,
        'country': value,
        'longitude': value,
        'latitude': value,
        'phone': value,
        'website_url': value,
        'updated_at': value,
        'created_at': value
    }
    assert v.validate(response_get.json(), schema)

@pytest.mark.parametrize("end_point", ['https://api.openbrewerydb.org/breweries/autocomplete?query=dog'])
def test_brewery_autocomplete(response_get, end_point):
    schema = {
        "id": {'type': 'string'},
        "name": {'type': 'string'}
    }
    assert v.validate(response_get.json()[0], schema)

@pytest.mark.parametrize('end_point', ["https://api.openbrewerydb.org/breweries/search?query=Flix_Brewhouse"])
def test_brewery_search(response_get, end_point):
    value = {"type": 'string', 'nullable': True}
    schema = {
        'id': {"type": "integer"},
        'name': {'type': 'string', 'regex': "Flix Brewhouse"},
        'obdb_id': value,
        'brewery_type': value,
        'street': value,
        'address_2': value,
        'address_3': value,
        'city': value,
        'county_province': value,
        'state': value,
        'postal_code': value,
        'country': value,
        'longitude': value,
        'latitude': value,
        'phone': value,
        'website_url': value,
        'updated_at': value,
        'created_at': value
    }
    assert v.validate(response_get.json()[0], schema)

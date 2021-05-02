import requests

def test_url_status(base_url, set_status):
    assert requests.get(base_url) == set_status

import requests
from pytest import fixture


with open("/home/bender/work/otus_python_auto_qa/hw_3/test_jsonplaceholder_api/end_points", 'r') as params:
    list_params = params.readlines()
    list_endpoints = [i.strip('\n') for i in list_params]

@fixture(name="end_point", params=list_endpoints)
def get_end_point(request):
    yield request.param

@fixture
def response_get(end_point):
    return requests.get(end_point)  # response содержит уже все хедеры и тело
import requests
from pytest import fixture
from hw_3.src import get_end_points

with open("./end_points", 'r') as params:
    list_params = params.readlines()
    list_endpoints = [i.strip('\n') for i in list_params]

@fixture(name="end_point", params=list_endpoints)
def get_end_point(request):
    yield request.param

@fixture
def response_get(end_point):
    return requests.get(end_point)  # response содержит уже все хедеры и тд
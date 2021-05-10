import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--uurl',
        default='https://ya.ru',
        help='this is mast be ya.ru'
    )

    parser.addoption(
        '--sstatus',
        default=200,
        help='200 is default value'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--uurl')


@pytest.fixture
def set_status(request):
    return request.config.getoption('--sstatus')

import pytest
from base.const import *


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="prod", help="Choose environment: master or prod")


@pytest.fixture(scope="session")
def base_url(request):
    base_url = request.config.getoption("base_url")
    if base_url == "prod":
        return prod_url
    if base_url == "master":
        return master_url
    else:
        raise pytest.UsageError("--base_url should be master or prod")

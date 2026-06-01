import os

import pytest


@pytest.fixture
def base_url():
    return os.environ.get("BASE_URL", "http://192.168.31.117:5002")
import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    url = os.environ.get("BASE_URL", "").strip()
    return url if url else "http://192.168.31.117:5002"
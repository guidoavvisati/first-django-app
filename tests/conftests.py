import pytest
from pathlib import Path


@pytest.fixture
def PROJECT_ROOT():
    return Path(__file__).parent

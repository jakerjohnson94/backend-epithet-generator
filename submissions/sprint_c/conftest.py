from sprint_c.app import app as myapp
import pytest


@pytest.fixture
def app():
    app = myapp
    return app

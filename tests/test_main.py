import pytest
from app.main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_endpoint(client):
    """Test that the home route returns a 200 OK status."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevOps Sandbox API is live!" in response.data

def test_error_endpoint(client):
    """Test that our error endpoint correctly flags a 500 status."""
    response = client.get('/test-error')
    assert response.status_code == 500
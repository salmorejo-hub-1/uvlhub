import pytest

from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234')
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_sample_assertion(test_client):
    """
    Sample test to verify that the test framework and environment are working correctly.
    It does not communicate with the Flask application; it only performs a simple assertion to
    confirm that the tests in this module can be executed.
    """
    greeting = "Hello, World!"
    assert greeting == "Hello, World!", "The greeting does not coincide with 'Hello, World!'"


def test_api_configuration_page_get(test_client):
    """
    Tests access to the API configuration page via a GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/api/configuration")
    assert response.status_code == 200, "The API configuration page could not be accessed."
    assert b"Generate New API Token" in response.data, "The expected content is not present on the page"

    logout(test_client)


def test_api_dataset_list_unauthorized(test_client):
    """
    Tests access to the API dataset list page via a GET request without authentication.
    Expects a 401 Unauthorized status code.
    """
    response = test_client.get("/api/dataset/list")
    assert response.status_code == 401, "Expected 401 Unauthorized, but received a different status code."
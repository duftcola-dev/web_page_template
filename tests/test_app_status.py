from tests.utils import basic

def test_app_status(client):
    response = client.get("/status/app")
    basic.check_default_response(response)

def test_app_status_database(client):
    response = client.get("/status/database")
    basic.check_default_response(response)
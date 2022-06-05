from utils import default

def test_app_status(client):
    response = client.get("/status/app")
    default.check_default_response(response)

def test_app_status_database(client):
    response = client.get("/status/database")
    default.check_default_response(response)
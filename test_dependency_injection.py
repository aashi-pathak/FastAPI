from dependency_injection import app, get_db_session
from fastapi.testclient import TestClient

testing_db = ["Database for testing"]

def get_testing_db():
    return testing_db

app.dependency_overrides[get_db_session] = get_testing_db
client = TestClient(app)

def test_item_should_add_to_db():
    response = client.post("/items/?item=sugar")
    assert response.status_code == 200
    assert response.text == '{"message":"added item sugar"}'
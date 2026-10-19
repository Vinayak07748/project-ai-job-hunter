from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_home():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI Job Hunter API!",
                                "status": "Running"}


def test_health_check():
    
    response = client.get('/health')


    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}

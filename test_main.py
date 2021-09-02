from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


def test_read_items():
    response = client.get("/todo")

    assert response.status_code == 200
    assert response.json() == {
                            "data": [
                                {"id": 1,"activity": "read"},
                                {"id": 2,"activity": "eat"}
                            ]}

def test_create_inexistent_item():
    response = client.post("/create", json={"id" : 10000000, "activity" : "testing"})
    assert response.status_code == 201
    assert response.json() == {"data" : "Added correctly!"}
    

def test_create_existent_item():
    response = client.post("/create", json={"id" : 1, "activity" : "testing"})
    assert response.status_code == 400
    assert response.json() == {"detail" : "Item already present!"}


def test_update_inexistent_item():
    response = client.put("/update?id=10000", json={"activity" : "testing"})
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item not found!"}
    

def test_update_existent_item():
    response = client.put("/update?id=1", json={"activity" : "testing"})
    assert response.status_code == 200
    assert response.json() == {"data" : "Updated correctly!"}


def test_delete_inexistent_item():
    response = client.delete("/delete/100000000")
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item not found!"}
    

def test_delete_existent_item():
    response = client.delete("/delete/1")
    assert response.status_code == 200
    assert response.json() == {'data' : "Deleted!"}
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_greetings():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome":"Thank you for using our service!"}


def test_read_items():
    response = client.get("/list")

    assert response.status_code == 200
    assert response.json() == {
                            "data": [
                                {"item" : "bread", "qty" : 1},
                                {"item" : "milk", "qty" : 2}
                            ]}

def test_create_inexistent_item():
    response = client.post("/create", json={"item" : "new_item", "qty" : 10})
    assert response.status_code == 201
    assert response.json() == {"data" : "new_item added correctly!"}
    

def test_create_existent_item():
    response = client.post("/create", json={"item" : "bread", "qty" : 3})
    assert response.status_code == 400
    assert response.json() == {"detail" : "bread already present!"}


def test_update_inexistent_item():
    response = client.put("/update?item_name=fake_item&item_quantity=55")
    assert response.status_code == 404
    assert response.json() == {"detail" : "fake_item not found!"}
    

def test_update_existent_item():
    response = client.put("/update?item_name=milk&item_quantity=55")
    assert response.status_code == 200
    assert response.json() == {"data" : "milk correctly updated!"}


def test_delete_inexistent_item():
    response = client.delete("/delete/fake_name")
    assert response.status_code == 404
    assert response.json() == {"detail" : "fake_name not found!"}
    

def test_delete_existent_item():
    response = client.delete("/delete/milk")
    assert response.status_code == 200
    assert response.json() == {'data' : "milk correctly deleted!"}
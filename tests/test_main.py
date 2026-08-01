import pytest
from fastapi.testclient import TestClient
from src.main import app, expenses_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    # Clear the database before each test
    expenses_db.clear()

def test_add_expense():
    response = client.post(
        "/expenses",
        json={"title": "Coffee", "amount": 4.5, "category": "Food", "date": "2023-10-27"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Coffee"
    assert data["amount"] == 4.5
    assert data["category"] == "Food"
    assert "id" in data

def test_get_all_expenses():
    client.post("/expenses", json={"title": "Coffee", "amount": 4.5, "category": "Food", "date": "2023-10-27"})
    client.post("/expenses", json={"title": "Bus", "amount": 2.0, "category": "Transport", "date": "2023-10-27"})
    
    response = client.get("/expenses")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_filter_expenses_by_category():
    client.post("/expenses", json={"title": "Coffee", "amount": 4.5, "category": "Food", "date": "2023-10-27"})
    client.post("/expenses", json={"title": "Bus", "amount": 2.0, "category": "Transport", "date": "2023-10-27"})
    
    response = client.get("/expenses?category=Food")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "Food"

def test_get_total_expenses():
    client.post("/expenses", json={"title": "Coffee", "amount": 4.5, "category": "Food", "date": "2023-10-27"})
    client.post("/expenses", json={"title": "Burger", "amount": 10.5, "category": "Food", "date": "2023-10-27"})
    client.post("/expenses", json={"title": "Bus", "amount": 2.0, "category": "Transport", "date": "2023-10-27"})
    
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert response.json() == {"total": 17.0}
    
    response_cat = client.get("/expenses/total?category=Food")
    assert response_cat.status_code == 200
    assert response_cat.json() == {"total": 15.0}

def test_delete_expense():
    res = client.post("/expenses", json={"title": "Coffee", "amount": 4.5, "category": "Food", "date": "2023-10-27"})
    exp_id = res.json()["id"]
    
    del_res = client.delete(f"/expenses/{exp_id}")
    assert del_res.status_code == 204
    
    get_res = client.get("/expenses")
    assert len(get_res.json()) == 0

def test_delete_nonexistent_expense():
    del_res = client.delete("/expenses/invalid-id")
    assert del_res.status_code == 404

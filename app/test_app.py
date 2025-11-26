from app import app

def test_hello_endpoint():
    client = app.test_client()
    resp = client.get("/hello")
    assert resp.status_code == 200
    assert resp.get_json()["message"].startswith("Hello DevOps")


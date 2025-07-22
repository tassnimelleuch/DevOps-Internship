"""Test Flask routes."""
import json

def test_index_route(client):
    """Test homepage returns 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Todo" in response.data  # Check template renders

def test_add_task(client):
    """Test task creation via POST."""
    response = client.post("/add", 
        data={"content": "Test task"},
        follow_redirects=True)
    assert response.status_code == 200
    assert b"Test task" in response.data

def test_summarize_api(client):
    """Test JSON summarization endpoint."""
    response = client.post("/summarize",
        json={"text": "This is a long text to summarize."},
        headers={"Content-Type": "application/json"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "summary" in data
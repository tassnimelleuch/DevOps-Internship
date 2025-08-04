"""test summarizer module."""
from unittest.mock import patch
def test_summarize_post_success(client):
    """Test successful summarization"""
    with patch('app.summarize.get_summary', return_value="Test summary"):
        # Test JSON
        response = client.post('/summarize',
                            json={'text': 'Test'},
                            headers={'Content-Type': 'application/json'})
        assert response.status_code == 200
        assert 'summary' in response.json
        response = client.post('/summarize', data={'text': 'Test'})
        assert response.status_code == 200
def test_summarize_invalid_input(client):
    """Test empty text submission - should return 400"""
    # Test empty string
    response = client.post('/summarize', data={'text': ''})
    assert response.status_code == 400
    assert 'error' in response.json
    # Test missing text parameter
    response = client.post('/summarize')
    assert response.status_code == 400
def test_summarize_error_handling(client):
    """Test summarizer failures"""
    with patch('app.summarize.get_summary', side_effect=Exception("Error")):
        response = client.post('/summarize', data={'text': 'Test'})
        assert response.status_code == 200

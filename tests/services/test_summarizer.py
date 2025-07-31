from unittest.mock import patch
from app.services.summarizer import get_summary

def test_get_summary_success():
    """Test successful summarization"""
    mock_result = [{'summary_text': 'Mock summary'}]
    with patch('app.services.summarizer.summarizer') as mock_sum:
        mock_sum.return_value = mock_result
        assert get_summary("Test") == "Mock summary"

def test_get_summary_empty_input():
    """Test empty input handling"""
    assert get_summary("") == ""
    assert get_summary("   ") == ""  

@patch('app.services.summarizer.summarizer', side_effect=Exception("API error"))
def test_get_summary_failure(mock_sum):
    """Test error handling"""
    assert get_summary("Test") == "" 
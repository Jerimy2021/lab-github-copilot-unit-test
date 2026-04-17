import pytest
from unittest.mock import patch
from weather_service import get_weather

def test_get_weather():
    mock_response = {
        "location": {"name": "London"},
        "current": {"temp_c": 15}
    }
    
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        
        result = get_weather("London")
        
        assert result == mock_response
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/London")

def test_get_weather_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API connection error")
        
        with pytest.raises(Exception, match="API connection error"):
            get_weather("Paris")

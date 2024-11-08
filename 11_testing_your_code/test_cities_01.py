# 11-1. City, Country - test_cities.py
from city_functions import city_country

def test_city_country():
    """Test that the city_country function works as expected."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
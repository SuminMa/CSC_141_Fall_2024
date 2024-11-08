# 11-2. Population - test_cities_02.py
from city_functions_02 import city_country

def test_city_country():
    """Test that the city_country function works as expected without population."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    """Test that the city_country function works with population."""
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile – population 5000000'
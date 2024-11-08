# 11-2. Population - city_functions_02.py
def city_country(city, country, population=None):
    """Return a string in the format 'City, Country' or 'City, Country – population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
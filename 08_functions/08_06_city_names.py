# 8-6. City Names

# Write a function called city_country() that takes in the name of a city and its country.
def city_country(city, country):
    # It should return a string formatted like '"Santiago, Chile"'.
    print(f'"{city.title()}, {country.title()}"')

# Call the function with at least three city-country pairs
city_country('Seoul', 'South Korea')
city_country('Tokyo', 'Japan')
city_country('Paris', 'France')
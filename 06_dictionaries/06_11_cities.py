# 6-11. Cities
# Make a dictionary called cities
# Use the names of three cities as keys in my dictionary
# Create a dictionary of information about each city
# Include the country that the city is in, its approximate population, and one fact
cities = {
    'Seoul': {
        'country': 'South Korea',
        'population': '9.5 million',
        'fact': 'Seoul is home to the world’s fastest internet speeds.'
        },
    'Dallas': {
        'country': 'United States',
        'population': '1.3 million',
        'fact': 'Dallas is famous for its role in the oil and cotton industries.'
        },
    'Reading': {
        'country': 'United Kingdom',
        'population': 'approximately 230,000',
        'fact': 'Reading hosts one of the UK’s most famous annual music festivals.'
        }
    }

# Print the name of each city and all of the information you have stored about it
for city, info in cities.items():
    print(f"\n{city} is in {info['country']}, with a population of {info['population']}.")
    print(f"One fact about {city} is {info['fact']}")
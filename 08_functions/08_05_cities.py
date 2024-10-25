# 8-5. Cities

# Write a function called describe_city() that accepts the name of a city and its country.
# Give the parameter for the country a default value.
def describe_city(city, country='South Korea'):
    # Print a simple sentence.
    print(f"{city.title()} is in {country.title()}.")

# Call the function for three different cities.
# At least one of which is not in the default country.
describe_city('Seoul')
describe_city('Busan')
describe_city('Paris', 'France')

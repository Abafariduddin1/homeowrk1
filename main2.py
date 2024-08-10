country_capitals = {}

for i in range(5):
    country = input(f"Enter the name of country {i+1}: ")
    capital = input(f"Enter the capital of {country}: ")
    
    country_capitals[country] = capital

print("Country and their capitals:", country_capitals)

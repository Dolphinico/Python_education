from city_functions import get_city_name

print("Enter 'q' at any time to quit")
while True:
    country = input("\nGive me a country name please ")
    if country == 'q':
        break
    city = input("Give me a city name please ")
    if city == 'q':
        break
    population = input("Give me a number of population please ")
    if population == 'q':
        break
    sorted_name = get_city_name(country,city, population)
    print('\tNeatly formatted name: ' + sorted_name + '.')
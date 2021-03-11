def get_city_name(country, city, population = ''):
    """Получает имя города и страны"""
    sorted_name = country + ' ' + city + ' - ' + population
    if population:
        sorted_name = country + ' ' + city + ' ' + population
    else:
        sorted_name = country + ' ' + city
    return sorted_name.title()
    
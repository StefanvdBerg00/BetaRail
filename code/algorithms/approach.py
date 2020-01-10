import sys
import random
from classes import Traject

def random_city(cities):
    while True:
        city = cities[random.choice(list(cities.keys()))]
        if len(city.get_connections(False)) != 0:
            return city

def outer_city(cities):
    min_length = sys.maxsize

    for city in cities:
        length = len(cities[city].get_connections(False))
        if length < min_length and length != 0:
            min_length = length
            current_city = cities[city]

    return current_city

def centered_city(cities):
    max_length = 0

    for city in cities:
        length = len(cities[city].get_connections(False))
        if length > max_length:
            max_length = length
            current_city = cities[city]

    return current_city


def approach(schedule, method):
    while sum([len(city.get_connections(False)) for city in schedule.cities.values()]) != 0:
        if method == "random" or method == "overlay":
            current_city = random_city(schedule.cities)
        elif method == "centered":
            current_city = centered_city(schedule.cities)
        elif method == "outer":
            current_city = outer_city(schedule.cities)
        else:
            return

        start_city = current_city
        traject = Traject()
        traject.route.append(current_city)

        while traject.next_city or traject.reversible:
            traject.next_city = False

            if method == "overlay":
                available_connections = current_city.get_connections(False)
                unavailable_connections = current_city.get_connections(True)

                if random.random() < ((1 / len(current_city.connections)) * 0.3):
                    connections = unavailable_connections
                else:
                    connections = available_connections
            else:
                connections = current_city.get_connections(False)

            if len(connections) != 0:
                connection = random.choice(connections)
                if (traject.get_time() + connection.time < schedule.max_time) and connection not in traject.connections:
                    traject.add(connection)
                    current_city = current_city.new_current(connection)
                    traject.route.append(current_city)
                    traject.next_city = True

            if not traject.next_city:
                current_city = start_city
                traject.connections.reverse()
                traject.reversible = False

        schedule.trajects.append(traject)

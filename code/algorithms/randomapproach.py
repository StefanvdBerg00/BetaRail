import random
from random import randrange
from classes import Traject

def random_city(cities):
    while True:
        city = cities[random.choice(list(cities.keys()))]
        if len([connection for connection in city.connections if not connection.visited]) != 0:
            return city

def randomapproach(schedule):
    while sum([len(city.get_available_connections()) for city in schedule.cities.values()]) != 0:
        current_city = random_city(schedule.cities)
        start_city = current_city
        traject = Traject()

        while traject.next_city or traject.reversible:
            traject.next_city = False
            connections = current_city.get_available_connections()

            if len(connections) != 0:
                connection = random.choice(connections)
                if (traject.get_time() + connection.time < schedule.max_time):
                    traject.add(connection)
                    current_city = current_city.new_current(connection)
                    traject.next_city = True

            if not traject.next_city:
                current_city = start_city
                traject.connections.reverse()
                traject.reversible = False

        schedule.trajects.append(traject)

import sys
import random
from classes import Traject


class Heuristic:
    def __init__(self, name, city_function, connections_function):
        self.name = name
        self.city_function = city_function
        self.connections_function = connections_function
        self.schedule = None
        self.current_city = None
        self.connections = None

    def random_city(self):
        while True:
            city = self.schedule.cities[random.choice(list(self.schedule.cities.keys()))]
            if len(city.get_connections(False)) != 0:
                self.current_city = city
                return

    def outer_city(self):
        min_length = sys.maxsize
        for city in self.schedule.cities:
            length = len(self.schedule.cities[city].get_connections(False))
            if length < min_length and length != 0:
                min_length = length
                current_city = self.schedule.cities[city]
        self.current_city = current_city

    def centered_city(self):
        max_length = 0
        for city in self.schedule.cities:
            length = len(self.schedule.cities[city].get_connections(False))
            if length > max_length:
                max_length = length
                current_city = self.schedule.cities[city]
        self.current_city = current_city

    def overlay_connections(self):
        available_connections = self.current_city.get_connections(False)
        unavailable_connections = self.current_city.get_connections(True)

        if random.random() < ((1 / len(self.current_city.connections)) * 0.3):
            connections = unavailable_connections
        else:
            connections = available_connections
        self.connections = connections

    def new_connections(self):
        connections = {}
        for connection in self.current_city.get_connections(False):
            next_city = self.current_city.new_current(connection)
            value = len(next_city.get_connections(False)) - 1
            if value in connections.keys():
                connections[value].append(connection)
            else:
                connections[value] = [connection]
        self.connections = connections[min(connections.keys())] if len(connections) != 0 else []

    def general_connections(self):
        self.connections = self.current_city.get_connections(False)

    def run(self):
        while sum([len(city.get_connections(False)) for city in self.schedule.cities.values()]) != 0:
            self.city_function(self)
            start_city = self.current_city
            traject = Traject()
            traject.route.append(self.current_city)

            while traject.next_city or traject.reversible:
                traject.set_next_city(False)
                self.connections_function(self)

                if len(self.connections) != 0:
                    connection = random.choice(self.connections)
                    if (traject.get_time() + connection.time < self.schedule.max_time) and connection not in traject.connections:
                        traject.add(connection)
                        self.current_city = self.current_city.new_current(connection)
                        traject.route.append(self.current_city)
                        traject.set_next_city(True)

                if not traject.next_city:
                    self.current_city = start_city
                    traject.reverse()

            self.schedule.trajects.append(traject)

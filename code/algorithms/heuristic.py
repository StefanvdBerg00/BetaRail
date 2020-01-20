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

    def random_city(self):
        while True:
            city = self.schedule.get_cities()[random.choice(list(self.schedule.get_cities().keys()))]
            if len(city.get_connections(False)) != 0:
                self.current_city = city
                return

    def outer_city(self):
        min_length = sys.maxsize
        for city in self.schedule.get_cities():
            length = len(self.schedule.get_cities()[city].get_connections(False))
            if length < min_length and length != 0:
                min_length = length
                current_city = self.schedule.get_cities()[city]
        self.current_city = current_city

    def centered_city(self):
        max_length = 0
        for city in self.schedule.get_cities():
            length = len(self.schedule.get_cities()[city].get_connections(False))
            if length > max_length:
                max_length = length
                current_city = self.schedule.get_cities()[city]
        self.current_city = current_city

    def overlay_connections(self):
        available_connections = self.current_city.get_connections(False)
        unavailable_connections = self.current_city.get_connections(True)

        if random.random() < ((1 / len(self.current_city.connections)) * 0.3):
            connections = unavailable_connections
        else:
            connections = available_connections
        return connections

    def new_connections(self):
        connections = {}
        for connection in self.current_city.get_connections(False):
            next_city = self.current_city.new_current(connection)
            value = len(next_city.get_connections(False)) - 1
            if value in connections.keys():
                connections[value].append(connection)
            else:
                connections[value] = [connection]
        return connections[min(connections.keys())] if len(connections) != 0 else []

    def general_connections(self):
        return self.current_city.get_connections(False)

    def run(self):
        while sum([len(city.get_connections(False)) for city in self.schedule.get_cities().values()]):
            self.city_function(self)
            start_city = self.current_city
            traject = Traject()

            while traject.get_next_city() or traject.get_reversible():
                traject.set_next_city(False)

                connections = self.connections_function(self)
                if len(connections) != 0:
                    connection = random.choice(connections)

                    if (traject.get_time() + connection.get_time() < self.schedule.get_max_time()) and connection not in traject.get_connections():
                        traject.add(connection)
                        self.current_city = self.current_city.new_current(connection)
                        traject.set_next_city(True)

                if not traject.get_next_city():
                    self.current_city = start_city
                    traject.reverse()

            self.schedule.add_traject(traject)

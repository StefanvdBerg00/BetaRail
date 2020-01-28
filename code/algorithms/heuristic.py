# ****************************************************************************
# heuristic.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ****************************************************************************

import sys, random
from traject import Traject


class Heuristic:
    def __init__(self, name, city_function, connections_function):
        self.name = name
        self.city_function = city_function
        self.connections_function = connections_function
        self.schedule = None
        self.current_city = None

    def random_city(self):
        """ Returns random city with at least 1 unvisited connection. """

        while True:
            city = self.schedule.get_cities()[random.choice(list(self.schedule.get_cities().keys()))]

            if len(city.get_connections(False)) != 0:
                self.current_city = city
                return

    def outer_city(self):
        """ Returns city with least unvisited connections. """

        min_length = sys.maxsize

        for city in self.schedule.get_cities():
            length = len(self.schedule.get_cities()[city].get_connections(False))

            if length < min_length and length != 0:
                min_length = length
                current_city = self.schedule.get_cities()[city]

        self.current_city = current_city

    def centered_city(self):
        """ Returns city with most unvisited connections. """

        max_length = 0

        for city in self.schedule.get_cities():
            length = len(self.schedule.get_cities()[city].get_connections(False))
            if length > max_length:
                max_length = length
                current_city = self.schedule.get_cities()[city]

        self.current_city = current_city

    def overlay_connections(self):
        """ Returns visited or unvisited connections based on probability distribution. """

        unvisited_connections = self.current_city.get_connections(False)
        visited_connections = self.current_city.get_connections(True)

        # The value 0.3 determines the probability distribution
        if random.random() < (0.3 / len(self.current_city.get_all_connections())):
            connections = visited_connections
        else:
            connections = unvisited_connections

        return connections

    def least_connections(self):
        """ Returns connections of the next current city with the least connections. """

        connections = {}

        for connection in self.current_city.get_connections(False):
            next_city = self.current_city.new_current(connection)

            # Amount of unvisited connections, ignoring connection which you came from
            value = len(next_city.get_connections(False)) - 1

            # Fill dictionary with amount of unvisited connections as key
            if value in connections.keys():
                connections[value].append(connection)
            else:
                connections[value] = [connection]

        return connections[min(connections.keys())] if len(connections) else []

    def general_connections(self):
        """ Returns connections of the current city. """

        return self.current_city.get_connections(False)

    def run(self):
        """ Fills schedule with trajects. """

        # Run algorithm until all connections are visited
        while sum([len(city.get_connections(False)) for city in self.schedule.get_cities().values()]):
            self.city_function(self)
            start_city = self.current_city
            traject = Traject()

            # Run until no cities can be connected to traject
            while traject.get_next_city() or traject.get_reversible():
                traject.set_next_city(False)
                connections = self.connections_function(self)

                if len(connections):
                    connection = random.choice(connections)

                    # Add connection to traject if constraints are satisfied
                    if (traject.get_time() + connection.get_time() < self.schedule.get_max_time()) \
                    and connection not in traject.get_connections():
                        traject.add(connection)
                        self.current_city = self.current_city.new_current(connection)
                        traject.set_next_city(True)

                # Reverse direction of traject if no city added
                if not traject.get_next_city():
                    self.current_city = start_city
                    traject.reverse()

            if len(traject.get_connections()):
                self.schedule.add_traject(traject)

# ****************************************************************************
# traject.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ****************************************************************************


class Traject:
    def __init__(self):
        self.connections = []
        self.time = 0
        self.reversible = True
        self.next_city = True

    def get_connections(self):
        """ Returns all connection in traject. """
        return self.connections

    def set_connections(self, value):
        """ Sets connections by a given list. """
        self.connections = value

    def get_time(self):
        """ Returns the time of traject. """
        return self.time

    def set_time(self, value):
        """ Sets the time of traject by a given number """
        self.time = value

    def get_reversible(self):
        """ Returns reversible of traject. """
        return self.reversible

    def get_next_city(self):
        """ Returns next_city of traject. """
        return self.next_city

    def set_next_city(self, value):
        """ Sets next_city by given value. """
        self.next_city = value

    def add(self, connection):
        """ Adds connection to traject. """
        self.connections.append(connection)
        connection.visited = True
        self.time += connection.time

    def reverse(self):
        """ Reverses the connection list in traject. """
        self.connections.reverse()
        self.reversible = False

    def remove_traject(self, schedule):
        """ Removes traject from schedule. """
        schedule.trajects.remove(self)

    def can_connect(self, city, connections):
        """ Checks if given city is at the edge of traject. """
        route = self.get_route()
        if (city == route[0] or city == route[-1]):
            return True
        return False

    def get_route(self):
        """ Returns the route for traject. """
        if len(self.connections) == 1:
            return [self.connections[0].get_city1(), self.connections[0].get_city2()]

        if self.connections[0].get_city1() != self.connections[1].get_city1() \
        and self.connections[0].get_city1() != self.connections[1].get_city2():
            city = self.connections[0].get_city1()
        else:
            city = self.connections[0].get_city2()

        route = [city]

        for connection in self.connections:
            city = city.new_current(connection)
            route.append(city)
        return route

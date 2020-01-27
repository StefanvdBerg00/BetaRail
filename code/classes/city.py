# ****************************************************************************
# city.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/


class City:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.x = None
        self.y = None

    def get_name(self):
        """ Returns name of city. """
        return self.name

    def get_x(self):
        """ Returns x coordinate of city. """
        return self.x

    def get_y(self):
        """ Returns y coordinate of city. """
        return self.y

    def get_connections(self, visited):
        """ Returns a list of connections where visited is True or False. """
        return [connection for connection in self.connections if connection.visited == visited]

    def get_all_connections(self):
        """ Returns all connections. """
        return self.connections

    def add(self, connection):
        """ Adds a connection to city. """
        self.connections.append(connection)

    def new_current(self, connection):
        """ Returns the other city in connection. """
        if connection.get_city1() == self:
            return connection.get_city2()
        return connection.get_city1()

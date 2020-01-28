# ****************************************************************************
# connection.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ****************************************************************************


class Connection:
    def __init__(self, city1, city2, time):
        self.city1 = city1
        self.city2 = city2
        self.time = time
        self.visited = False

    def get_city1(self):
        """ Returns one city from connection. """
        return self.city1

    def get_city2(self):
        """ Returns other city from connection. """
        return self.city2

    def get_time(self):
        """ Returns the time of connection. """
        return self.time

    def get_visited(self):
        """ Returns visited of connection. """
        return self.visited

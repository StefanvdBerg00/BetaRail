# ****************************************************************************
# classes.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import csv


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
    #
    # def remove_connection(self, connection):
    #     """ Removes a connection from city. """
    #     self.connections.remove(connection)

    def __repr__(self):
        return f"{self.name}"


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

    def __repr__(self):
        return f"From {self.city1} to {self.city2} ({self.time} min)"


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
        # for connection in self.connections:
        #     connection.city1.remove_connection(connection)
        #     connection.city2.remove_connection(connection)
        #     schedule.remove_connection(connection)
        schedule.trajects.remove(self)

    def can_connect(self, city, connections):
        """ Checks if given city is at the edge of traject. """
        route = self.get_route()
        if (city == route[0] or city == route[-1]): #and not any(connection in connections for connection in self.connections):
            return True
        return False

    def get_route(self):
        """ Returns the route for traject. """
        if len(self.connections) == 1:
            return [self.connections[0].get_city1(), self.connections[0].get_city2()]

        city = self.connections[0].get_city1() if self.connections[0].get_city1() != self.connections[1].get_city1() and self.connections[0].get_city1() != self.connections[1].get_city2() else self.connections[0].get_city2()
        route = [city]

        for connection in self.connections:
            city = city.new_current(connection)
            route.append(city)
        return route

    def __repr__(self):
        return f"{self.connections}\n"


class Schedule:
    def __init__(self, data, max_time):
        self.trajects = []
        self.all_connections = data["all_connections"]
        self.number_connections = len(self.all_connections)
        self.cities = data["cities"]
        self.max_time = max_time

    def get_trajects(self):
        """ Returns all trajects in schedule. """
        return self.trajects

    def get_cities(self):
        """ Returns all cities in schedule. """
        return self.cities

    def get_max_time(self):
        """ Returns the maximum time of a traject. """
        return self.max_time

    def add_traject(self, traject):
        """ Adds a traject to schedule. """
        self.trajects.append(traject)

    # def remove_connection(self, connection):
    #     """ Removes a connection from all the connection. """
    #     if sum([1 for traject in self.trajects if connection in traject.get_connections()]) == 1:
    #         self.all_connections.remove(connection)

    def quality(self):
        """ Returns the quality of schedule. """
        T = len(self.trajects)
        Min = sum([traject.get_time() for traject in self.trajects])
        connections = []
        [connections.extend(connection) for connection in [traject.get_connections() for traject in self.trajects]]
        p = len(set(connections)) / self.number_connections
        # p = len([connection for connection in self.all_connections if connection.get_visited()]) / self.number_connections
        return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 + Min)}

    def create_csv(self):
        """ Creates a csv-file for schedule. """    
        with open('results/solution.csv', mode="w", newline="") as solution_file:
            solution_writer = csv.writer(solution_file, delimiter=",")
            solution_writer.writerow(["trein", "lijnvoering"])

            for i, traject in enumerate(self.trajects):
                solution_writer.writerow([f"trein_{i + 1}", traject.get_route()])

    def __repr__(self):
        return "".join([f"{traject.get_route()}\n" for traject in self.trajects])

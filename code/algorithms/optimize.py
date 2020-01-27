# ****************************************************************************
# optimize.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import copy
from traject import Traject


class Node:
    def __init__(self, city, connection, prev_node):
        self.city = city
        self.connection = connection
        self.prev_node = prev_node

    def get_city(self):
        """ Returns city of node. """
        return self.city

    def length(self):
        """ Returns length of connected nodes. """
        if self.prev_node:
            return self.connection.get_time() + self.prev_node.length()
        return 0

    def connections(self):
        """ Returns list of connections from connected nodes. """
        if self.prev_node:
            list = self.prev_node.connections()
            list.append(self.connection)
            return list
        return []

    def start_node(self):
        """ Returns city of the first node. """
        if self.prev_node:
            return self.prev_node.start_node()
        return self

    def __repr__(self):
        if self.prev_node:
            return f"{self.city} -{self.length()}->{self.prev_node}"
        return f"{self.connection}"


class Optimize:
    def __init__(self, schedule, depth):
        self.stack = []
        self.traject = None
        self.schedule = schedule
        self.depth = depth
        self.shortest = {"time": 0}

    def run(self):
        """ Optimizes schedule by merging trajects. """

        # Run until schedule not improved
        while self.shortest["time"] != 100:
            self.shortest = {"time": 100, "state": None, "old_trajects": []}

            # Find best merge of all trajects
            for traject in self.schedule.get_trajects():
                route = traject.get_route()
                self.traject = traject
                self.DepthFirst(route[0])
                self.DepthFirst(route[-1])

            state = self.shortest["state"]

            if state:
                traject_0 = self.shortest["old_trajects"][0]
                traject_1 = self.shortest["old_trajects"][1]

                # Decide to merge two trajects or delete one
                if (state.length() + traject_0.get_time()) \
                < ((len(traject_0.get_connections()) / self.schedule.number_connections) * 10000):
                    traject = Traject()
                    traject.set_time(state.length() + traject_0.get_time() + traject_1.get_time())

                    if state.get_city() != traject_1.get_route()[0]:
                        traject_1.reverse()

                    if state.start_node().get_city() != traject_0.get_route()[-1]:
                        traject_0.reverse()

                    traject.set_connections(traject_0.get_connections() + state.connections() \
                                          + traject_1.get_connections())

                    self.schedule.trajects.remove(traject_0)
                    self.schedule.trajects.remove(traject_1)
                    self.schedule.add_traject(traject)
                else:
                    traject_0.remove_traject(self.schedule)

        # Delete traject if score improves
        for traject in self.schedule.get_trajects():
            if 100 + traject.get_time() \
            > ((len(traject.get_connections()) / self.schedule.number_connections) * 10000):
                traject.remove_traject(self.schedule)

    def DepthFirst(self, city):
        """ Performs depth first algorithm, starting from a given city. """

        self.stack.append(Node(city, None, None))

        # Run until no new states available
        while len(self.stack) > 0:
            state = self.stack.pop()

            # Iterate over every traject except itself
            for traject in [traject for traject in self.schedule.get_trajects() if traject != self.traject]:

                # Remember best merge where constraints were satisfied
                if state.length() < self.shortest["time"] and traject.get_time() + state.length() \
                + self.traject.get_time() < self.schedule.get_max_time() \
                and traject.can_connect(state.get_city(), state.connections()):
                    self.shortest = {"time": state.length(),
                                     "state": state,
                                     "old_trajects": [self.traject, traject]}

            # Create next layer
            if len(state.connections()) < self.depth and state.length() < self.shortest["time"]:
                for connection in [connection for connection in state.city.get_all_connections()]:
                    node = Node(state.city.new_current(connection), connection, state)
                    self.stack.append(node)

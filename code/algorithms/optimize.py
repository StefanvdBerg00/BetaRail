import copy
from classes import Traject


class Node:
    def __init__(self, city, connection, prev_node):
        self.city = city
        self.connection = connection
        self.prev_node = prev_node

    def length(self):
        if self.prev_node:
            return self.connection.get_time() + self.prev_node.length()
        return 0

    def connections(self):
        if self.prev_node:
            list = self.prev_node.connections()
            list.append(self.connection)
            return list
        return []

    def start_node(self):
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
        while self.shortest["time"] != 100:
            self.shortest = {"time": 100, "state": None, "old_trajects": []}

            for traject in self.schedule.get_trajects():
                route = traject.get_route()
                self.traject = traject
                self.DepthFirst(route[0])
                self.DepthFirst(route[-1])

            if self.shortest["state"]:
                traject = Traject()
                traject.time = self.shortest["state"].length() + self.shortest["old_trajects"][0].get_time() + self.shortest["old_trajects"][1].get_time()

                if self.shortest["state"].city != self.shortest["old_trajects"][1].get_route()[0]:
                    self.shortest["old_trajects"][1].connections.reverse()
                if self.shortest["state"].start_node().city != self.shortest["old_trajects"][0].get_route()[-1]:
                    self.shortest["old_trajects"][0].connections.reverse()

                traject.connections = self.shortest["old_trajects"][0].connections + self.shortest["state"].connections() + self.shortest["old_trajects"][1].connections
                self.schedule.trajects.remove(self.shortest["old_trajects"][0])
                self.schedule.trajects.remove(self.shortest["old_trajects"][1])
                self.schedule.add_traject(traject)

    def DepthFirst(self, city):
        self.stack.append(Node(city, None, None))

        while len(self.stack) > 0:
            state = self.stack.pop()

            for traject in [traject for traject in self.schedule.get_trajects() if traject != self.traject]:
                if state.length() < self.shortest["time"] and traject.get_time() + state.length() + self.traject.get_time() < self.schedule.get_max_time() and traject.can_connect(state.city, state.connections()):
                    self.shortest = {"time": state.length(), "state": state, "old_trajects": [self.traject, traject]}

            if len(state.connections()) < self.depth and state.length() < self.shortest["time"]: #
                for connection in [connection for connection in state.city.connections]: #if connection not in state.connections() and connection not in self.traject.connections]:
                    node = Node(state.city.new_current(connection), connection, state)
                    self.stack.append(node)
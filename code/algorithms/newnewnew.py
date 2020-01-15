import copy
from classes import Traject


class Node:
    def __init__(self, city, connection, prev_node):
        self.city = city
        self.connection = connection
        self.prev_node = prev_node

    def length(self):
        if self.prev_node:
            return self.connection.time + self.prev_node.length()
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

            for traject in self.schedule.trajects:
                self.traject = traject
                self.DepthFirst(traject.route[0])
                self.DepthFirst(traject.route[-1])

            if self.shortest["state"]:
                # print(f"SCHEDULE BEFORE:\n {self.schedule}\n")
                # print("Trying to connect:")
                # print(f"STATE: {self.shortest['state'].connections()}")
                # print(f"TRAJECT1: {self.shortest['old_trajects'][0]}")
                # print(f"TRAJECT2: {self.shortest['old_trajects'][1]}")
                #
                # print(f"TIMES: {self.shortest['state'].length()} + {self.shortest['old_trajects'][0].time} + {self.shortest['old_trajects'][1].time}")

                traject = Traject()
                traject.time = self.shortest["state"].length() + self.shortest["old_trajects"][0].time + self.shortest["old_trajects"][1].time

                if self.shortest["state"].city != self.shortest["old_trajects"][1].route[0]:
                    self.shortest["old_trajects"][1].connections.reverse()
                if self.shortest["state"].start_node().city != self.shortest["old_trajects"][0].route[-1]:
                    self.shortest["old_trajects"][0].connections.reverse()

                new_connections = self.shortest["old_trajects"][0].connections + self.shortest["state"].connections() + self.shortest["old_trajects"][1].connections
                traject.connections = new_connections

                start_city = new_connections[0].city1 if new_connections[0].city1 != new_connections[1].city1 and new_connections[0].city1 != new_connections[1].city2 else new_connections[0].city2
                new_route = [start_city]
                for connection in new_connections:
                    start_city = start_city.new_current(connection)
                    new_route.append(start_city)

                traject.route = new_route

                # print(f"NEW TRAJECT: {traject}")
                # print(f"NEW ROUTE: {traject.route}")
                # print(f"NEW TIME: {traject.time}")

                self.schedule.trajects.remove(self.shortest["old_trajects"][0])
                self.schedule.trajects.remove(self.shortest["old_trajects"][1])
                self.schedule.trajects.append(traject)

                # print(f"SCHEDULE AFTER:\n {self.schedule}\n")

    def DepthFirst(self, city):
        self.stack.append(Node(city, None, None))

        while len(self.stack) > 0:
            state = self.stack.pop()

            for traject in [traject for traject in self.schedule.trajects if traject != self.traject]:
                if state.length() < self.shortest["time"] and traject.time + state.length() + self.traject.time < self.schedule.max_time and traject.can_connect2(state.city, state.connections()):
                    self.shortest = {"time": state.length(), "state": state, "old_trajects": [self.traject, traject]}

            if len(state.connections()) < self.depth and state.length() < self.shortest["time"]:
                for connection in [connection for connection in state.city.connections if connection not in state.connections() and connection not in self.traject.connections]:
                    node = Node(state.city.new_current(connection), connection, state)
                    self.stack.append(node)

import random


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


class Tree:
    def __init__(self, schedule):
        self.lines = []
        self.schedule = schedule

    def create_tree(self, node, n, illegal_connections):
        if n < 6:
            n += 1

            finished = True
            for connection in node.city.connections:
                if connection not in illegal_connections:
                    if node not in self.lines:
                        self.lines.append(node)

                    finished = False
                    illegal_connections.append(connection)
                    self.create_tree(Node(node.city.new_current(connection), connection, node), n, illegal_connections)

            if finished and node.prev_node:
                self.lines.append(node)
        else:
            if node not in self.lines:
                self.lines.append(node)

    def __repr__(self):
        return f"{self.lines}"


def optimize(schedule):
    best = {"traject_1": None}
    while "traject_1" in best.keys():
        best = {"time": 100}

        for traject in schedule.trajects:
            tree = Tree(schedule)

            illegal_connections = [connection for connection in traject.connections]
            start_connection_1 = traject.connections[0]
            start_city_1 = start_connection_1.city1 if start_connection_1.city1 == traject.route[0] or start_connection_1.city1 == traject.route[-1] else start_connection_1.city2

            start_connection_2 = traject.connections[-1]
            if start_connection_2 == start_connection_1:
                start_city_2 = start_city_1.new_current(start_connection_1)
            else:
                start_city_2 = start_connection_2.city1 if start_connection_2.city1 == traject.route[0] or start_connection_2.city1 == traject.route[-1] else start_connection_2.city2

            tree.create_tree(Node(start_city_1, start_connection_1, None), 0, illegal_connections)
            tree.create_tree(Node(start_city_2, start_connection_2, None), 0, illegal_connections)

            for traject2 in schedule.trajects:
                for node in tree.lines:
                    connections = node.connections()
                    time = sum([connection.time for connection in connections])
                    total_time = traject.time + traject2.time + time

                    if traject2 != traject and traject.can_connect(node.start_node().city, connections) and traject2.can_connect(node.city, connections) and total_time < schedule.max_time and time < best["time"]:
                        best = {"traject_1": traject, "traject_2": traject2, "added": node, "time": time, "total_time": total_time, "info": [connections, traject2 != traject, traject.can_connect(node.city, connections), traject2.can_connect(node.city, connections)]}

        if "traject_1" in best.keys():
            # print("----------------OPTIMIZING-----------------")
            # print(f"{best}\n")
            #
            # print(best["traject_1"].route)
            # print(best["traject_2"].route)
            #
            # print(best["info"])
            #
            # print(f"SCHEDULE BEFORE:\n {schedule}\n")

            new_connections = best["added"].connections()
            if best["added"].city == best["traject_2"].connections[0].city1 or best["added"].city == best["traject_2"].connections[0].city2:
                new_connections += best["traject_2"].connections
            else:
                best["traject_2"].connections.reverse()
                new_connections += best["traject_2"].connections
            if best["added"].start_node().connection == best["traject_1"].connections[0]:
                best["traject_1"].connections.reverse()
                new_connections = best["traject_1"].connections + new_connections
            else:
                new_connections = best["traject_1"].connections + new_connections

            best["traject_1"].connections = new_connections
            best["traject_1"].time = best["total_time"]

            if len(new_connections) > 1:
                new_route = []
                start_city = new_connections[0].city1
                if new_connections[1].city1 == start_city or new_connections[1].city2 == start_city:
                    start_city = start_city.new_current(new_connections[0])
                new_route.append(start_city)

                for connection in new_connections:
                    start_city = start_city.new_current(connection)
                    new_route.append(start_city)
            else:
                new_route = [new_connections[0].city1, new_connections[0].city2]

            best["traject_1"].route = new_route

            # print(best["traject_1"].connections)
            # print(best["traject_1"].route)

            schedule.trajects.remove(best["traject_2"])
            # print(f"SCHEDULE AFTER:\n {schedule}\n")

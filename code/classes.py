import csv


class City:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.x = None
        self.y = None

    def get_connections(self, visited):
        return [connection for connection in self.connections if connection.visited == visited]

    def get_all_connections(self):
        return self.connections

    def add(self, connection):
        self.connections.append(connection)

    def new_current(self, connection):
        if connection.city1 == self:
            return connection.city2
        return connection.city1

    def remove_connection(self, connection):
        self.connections.remove(connection)

    def __repr__(self):
        return f"{self.name}"


class Connection:
    def __init__(self, city1, city2, time):
        self.city1 = city1
        self.city2 = city2
        self.time = time
        self.visited = False

    def get_time(self):
        return self.time

    def get_visited(self):
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
        return self.connections

    def set_connections(self, value):
        self.connections = value

    def get_time(self):
        return self.time

    def set_time(self, value):
        self.time = value

    def get_reversible(self):
        return self.reversible

    def get_next_city(self):
        return self.next_city

    def set_next_city(self, value):
        self.next_city = value

    def add(self, connection):
        self.connections.append(connection)
        connection.visited = True
        self.time += connection.time

    def reverse(self):
        self.connections.reverse()
        self.reversible = False

    def remove_traject(self, schedule):
        for connection in self.connections:
            connection.city1.remove_connection(connection)
            connection.city2.remove_connection(connection)
            schedule.remove_connection(connection)
        schedule.trajects.remove(self)

    def can_connect(self, city, connections):
        route = self.get_route()
        if (city == route[0] or city == route[-1]): #and not any(connection in connections for connection in self.connections):
            return True
        return False

    def get_route(self):
        if len(self.connections) == 1:
            return [self.connections[0].city1, self.connections[0].city2]

        city = self.connections[0].city1 if self.connections[0].city1 != self.connections[1].city1 and self.connections[0].city1 != self.connections[1].city2 else self.connections[0].city2
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
        return self.trajects

    def get_cities(self):
        return self.cities

    def get_max_time(self):
        return self.max_time

    def add_traject(self, traject):
        self.trajects.append(traject)

    def remove_connection(self, connection):
        if sum([1 for traject in self.trajects if connection in traject.get_connections()]) == 1:
            self.all_connections.remove(connection)

    def quality(self):
        T = len(self.trajects)
        Min = sum([traject.get_time() for traject in self.trajects])
        p = len([connection for connection in self.all_connections if connection.get_visited()]) / self.number_connections
        return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 + Min)}

    def create_csv(self):
        with open('results/solution.csv', mode="w", newline="") as solution_file:
            solution_writer = csv.writer(solution_file, delimiter=",")
            solution_writer.writerow(["trein", "lijnvoering"])

            for i, traject in enumerate(self.trajects):
                solution_writer.writerow([f"trein_{i + 1}", traject.get_route()])

    def __repr__(self):
        return "".join([f"{traject.get_route()}\n" for traject in self.trajects])

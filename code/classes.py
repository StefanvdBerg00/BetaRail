class City:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.x = None
        self.y = None

    def add(self, connection):
        self.connections.append(connection)

    def new_current(self, connection):
        if connection.city1 == self:
            return connection.city2
        return connection.city1

    def get_available_connections(self):
        return [connection for connection in self.connections if not connection.visited]

    def __repr__(self):
        return f"{self.name}"


class Connection:
    def __init__(self, city1, city2, time):
        self.city1 = city1
        self.city2 = city2
        self.time = time
        self.visited = False

    def __repr__(self):
        return f"From {self.city1} to {self.city2} ({self.time} min)"


class Traject:
    def __init__(self):
        self.connections = []
        self.time = 0
        self.reversible = True
        self.next_city = True

    def add(self, connection):
        self.connections.append(connection)
        connection.visited = True
        self.time += connection.time

    def get_time(self):
        return self.time

    def __repr__(self):
        return f"{self.connections}\n"


class Schedule:
    def __init__(self, data, max_time):
        self.trajects = []
        self.all_connections = data["all_connections"]
        self.cities = data["cities"]
        self.max_time = max_time

    def quality(self):
        T = len(self.trajects)
        Min = sum([traject.get_time() for traject in self.trajects])
        p = len([connection for connection in self.all_connections if connection.visited]) / len(self.all_connections)
        return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 + Min)}

    def __repr__(self):
        return f"{self.trajects}"

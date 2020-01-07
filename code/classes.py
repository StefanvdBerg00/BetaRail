class City:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.x = None
        self.y = None

    def add(self, connection):
        self.connections.append(connection)

    def __str__(self):
        return f"{self.name}"

class Connection:
    def __init__(self, city1, city2, time):
        self.city1 = city1
        self.city2 = city2
        self.time = time
        self.visited = False

    def __str__(self):
        return f"From {self.city1} to {self.city2} ({self.time} min)"

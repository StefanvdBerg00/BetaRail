import csv

class City:
    def __init__(self, name):
        self.name = name
        self.connections = []

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

cities = {}
max_length = 0

with open("data/ConnectiesHolland.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        city1 = row[0]
        city2 = row[1]
        time = int(row[2])

        if city1 not in cities:
            cities[city1] = City(city1)
        if city2 not in cities:
            cities[city2] = City(city2)

        connection = Connection(cities[city1], cities[city2], time)
        cities[city1].add(connection)
        cities[city2].add(connection)

        if len(cities[city1].connections) > max_length:
            max_length = len(cities[city1].connections)
            current_city = cities[city1]
        if len(cities[city2].connections) > max_length:
            max_length = len(cities[city2].connections)
            current_city = cities[city2]

trajects = []

found = True
while found:
    start_city = current_city
    found = False
    time = 0
    route = []
    change = True

    while True:
        next = False
        prev_city = current_city
        for connection in current_city.connections:
            if connection not in route and (time + connection.time < 120) and not connection.visited:
                route.append(connection)
                connection.visited = True
                time += connection.time
                current_city = connection.city2 if connection.city2 != current_city else connection.city1
                next = True
                break

        if not next:
            if current_city == prev_city:
                if change:
                    current_city = start_city
                    route.reverse()
                    change = False
                else:
                    break

    trajects.append({"route":route, "time": time})

    for city in cities.values():
        for connection in city.connections:
            if not connection.visited:
                current_city = city
                found = True
                break

    print([f"{connection}" for connection in route])

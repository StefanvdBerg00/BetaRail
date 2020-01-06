import csv

class City:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add(self, destination, time):
        self.connections.append({"destination":destination, "time":time, "visited":False})

    def __str__(self):
        return f"{self.name}: {self.connections}"

class Connection:
    def __init__(self, city1, city2, time):
        self.city1 = city1
        self.city2 = city2
        self.time = time

    def __str__(self):
        return f"From {self.city1} to {self.city2} ({self.time} seconds)"        

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

        cities[city1].add(cities[city2], time)
        cities[city2].add(cities[city1], time)

        if len(cities[city1].connections) > max_length:
            max_length = len(cities[city1].connections)
            current_city = cities[city1]
        if len(cities[city2].connections) > max_length:
            max_length = len(cities[city2].connections)
            current_city = cities[city2]

trajects = []

found = True

while found:

    found = False
    time = 0 
    route = [current_city]
    change = True
    while True:
        next = False
        prev_city = current_city
        for connection in current_city.connections:
            
            if connection["destination"] not in route and time + connection["time"] < 120 and not connection["visited"]:
                route.append(connection["destination"])
                connection["visited"] = True
                destination = cities[connection["destination"].name]
                destination.connections["visited"] = True
                print (destination.name)
                time += connection["time"]
                current_city = connection["destination"]
                next = True
                break
        
        if not next:
            if current_city == prev_city:
                if change:
                    current_city = route[0]
                    route.reverse()
                    change = False
                else:
                    break

    trajects.append({"route":route, "time": time})

    
    for city in cities.values():
        for connection in city.connections:
            if not connection["visited"]:
                current_city = city
                found = True


    print ([city.name for city in route])
    print (time)


        






            
            
        
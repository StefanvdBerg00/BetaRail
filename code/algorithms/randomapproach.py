import random
from random import randrange

def random_city(cities):
    while True:
        city = cities[random.choice(list(cities.keys()))]
        if len([connection for connection in city.connections if not connection.visited]) != 0:
            return city

def randomapproach(cities, MAX_MIN):
    trajects = []

    found = True
    while found:
        current_city = random_city(cities)
        start_city = current_city
        found = False
        time = 0
        route = []
        change = True
        print("-------------------")
        print(current_city)
        print("-------------------")
        while True:
            next = False
            prev_city = current_city
            connections = [connection for connection in current_city.connections if not connection.visited]

            if len(connections) != 0:
                connection = connections[randrange(len(connections))]
                if (time + connection.time < MAX_MIN):
                    route.append(connection)
                    connection.visited = True
                    time += connection.time
                    current_city = connection.city2 if connection.city2 != current_city else connection.city1
                    next = True

            if not next:
                if current_city == prev_city:
                    if not change:
                        break

                    current_city = start_city
                    route.reverse()
                    change = False


        trajects.append({"route":route, "time": time})

        for city in cities.values():
            if len([connection for connection in city.connections if not connection.visited]) != 0:
                current_city = city
                found = True
                break

    return trajects

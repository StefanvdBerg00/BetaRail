def main_city(cities):
    max_length = 0

    for city in cities:
        length = len([connection for connection in cities[city].connections if not connection.visited])
        if length > max_length:
            max_length = length
            current_city = cities[city]

    return current_city

def centeredapproach(cities, MAX_MIN):
    trajects = []

    found = True
    while found:
        current_city = main_city(cities)
        start_city = current_city
        found = False
        time = 0
        route = []
        change = True

        while True:
            next = False
            for connection in current_city.connections:
                if (time + connection.time < MAX_MIN) and not connection.visited:
                    route.append(connection)
                    connection.visited = True
                    time += connection.time
                    current_city = connection.city2 if connection.city2 != current_city else connection.city1
                    next = True
                    break

            if not next:
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

import csv
from classes import City, Connection

def csvdata(connections_file, coordinates_file):
    cities = {}
    all_connections = []

    with open(connections_file) as csv_file:
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
            all_connections.append(connection)
            cities[city1].add(connection)
            cities[city2].add(connection)

    with open(coordinates_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            city = row[0]
            x = float(row[1])
            y = float(row[2])

            cities[city].x = x
            cities[city].y = y

    return {"cities": cities, "all_connections": all_connections}

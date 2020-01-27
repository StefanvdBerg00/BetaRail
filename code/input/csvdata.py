# ****************************************************************************
# csvdata.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import csv
from city import City
from connection import Connection

def csvdata(connections_file, coordinates_file, exclusion):
    """ Returns a dictionary with all data from csv files. """

    cities = {}
    all_connections = []

    # Read city's connections
    with open(connections_file) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            city1 = row[0]
            city2 = row[1]
            time = int(row[2])

            # Exclude given city
            if exclusion != city1 and exclusion != city2:
                if city1 not in cities:
                    cities[city1] = City(city1)
                if city2 not in cities:
                    cities[city2] = City(city2)

                connection = Connection(cities[city1], cities[city2], time)
                all_connections.append(connection)
                cities[city1].add(connection)
                cities[city2].add(connection)

    # Read city's coordinates
    with open(coordinates_file) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            city = row[0]
            x = float(row[1])
            y = float(row[2])

            if city in cities:
                cities[city].x = x
                cities[city].y = y

    return {"cities": cities, "all_connections": all_connections}

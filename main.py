import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection
from csvdata import csvdata
from centeredapproach import centeredapproach

def quality(trajects):
    T = len(trajects)
    Min = sum([traject["time"] for traject in trajects])
    p = len([connection for connection in all_connections if connection.visited]) / len(all_connections)
    return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 - Min)}

csvdata = csvdata()
cities = csvdata["cities"]
all_connections = csvdata["all_connections"]
max_length = 0

trajects = centeredapproach(cities)

visualisation(all_connections, quality(trajects))

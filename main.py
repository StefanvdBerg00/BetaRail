import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection
from csvdata import csvdata
from centeredapproach import centeredapproach
from outerapproach import outerapproach
from randomapproach import randomapproach

def quality(trajects):
    T = len(trajects)
    Min = sum([traject["time"] for traject in trajects])
    p = len([connection for connection in all_connections if connection.visited]) / len(all_connections)
    return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 + Min)}

MIN_180 = 180
MIN_120 = 120

csvdata = csvdata()
cities = csvdata["cities"]
all_connections = csvdata["all_connections"]

# trajects = centeredapproach(cities, MIN_180)

# trajects = outerapproach(cities, MIN_180)

trajects = randomapproach(cities, MIN_180)

for traject in trajects:
    print([f"{connection}" for connection in traject["route"]])

visualisation(trajects, quality(trajects))

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection, Schedule, Traject
from csvdata import csvdata
from centeredapproach import centeredapproach
from outerapproach import outerapproach
from randomapproach import randomapproach

MIN_180 = 180
MIN_120 = 120

# trajects = centeredapproach(cities, MIN_180)

# trajects = outerapproach(cities, MIN_180)

best = {"schedule": None, "K": 0}
for i in range(10000):
    schedule = Schedule(csvdata("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv"), MIN_180)
    randomapproach(schedule)
    quality = schedule.quality()

    if quality["K"] > best["K"]:
        best["schedule"] = schedule
        best["K"] = quality["K"]

visualisation(best["schedule"].trajects, best["schedule"].quality())

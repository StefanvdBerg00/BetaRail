import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection, Schedule, Traject
from csvdata import csvdata
from approach import approach

def run(connections_file, coordinates_file, N, max_time, method):
    best = {"schedule": None, "K": 0}

    print(f"{N}x {method}")
    for i in range(N):
        if i % (N // 100) == 0:
            # print("◘" * (i // (N // 100)), end="\r")
            print(f"{(i // (N // 100))}%", end="\r")

        schedule = Schedule(csvdata(connections_file, coordinates_file), max_time)
        approach(schedule, method)
        quality = schedule.quality()

        if quality["K"] > best["K"]:
            best["schedule"] = schedule
            best["K"] = quality["K"]

    return best


MIN_180 = 180
MIN_120 = 120

N = 100

A = "random"
B = "centered"
C = "outer"
D = "overlay"

solution = run("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv", N, MIN_180, C)

solution["schedule"].create_csv()

visualisation(solution["schedule"].trajects, solution["schedule"].quality())

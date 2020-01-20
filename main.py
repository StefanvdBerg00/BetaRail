import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection, Schedule, Traject
from csvdata import csvdata
from optimize import Optimize
from heuristic import Heuristic
from datetime import datetime
import time

def run(connections_file, coordinates_file, N, max_time, method, improve, depth):
    best = {"schedule": None, "K": 0}
    timings = []

    print(f"{N}x {method.name}")
    for i in range(N):
        if N >= 100 and i % (N // 100) == 0:
            print(f"{(i // (N // 100))}%", end="\r")

        start = time.time()

        method.schedule = Schedule(csvdata(connections_file, coordinates_file), max_time)
        method.run()

        if improve:
            optimize = Optimize(method.schedule, depth)
            optimize.run()

        quality = method.schedule.quality()

        if quality["K"] > best["K"]:
            best["schedule"] = method.schedule
            best["K"] = quality["K"]

        timings.append(int(round((time.time() - start) * 1000)))
        # print(f"estimated time: {round(((sum(timings)/len(timings)) * (N - i)) / 1000, 1)}", end="\r")

    # print(f"\nAVERAGE TIME: {sum(timings)/len(timings)} ms")

    return best


MIN_180 = 180
MIN_120 = 120

N = 1

A = Heuristic("random", Heuristic.random_city, Heuristic.general_connections)
B = Heuristic("centered", Heuristic.centered_city, Heuristic.general_connections)
C = Heuristic("outer", Heuristic.outer_city, Heuristic.general_connections)
D = Heuristic("overlay", Heuristic.random_city, Heuristic.overlay_connections)
E = Heuristic("new", Heuristic.random_city, Heuristic.new_connections)

IMPROVE = True
DEPTH = 4

solution = run("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv", N, MIN_180, E, IMPROVE, DEPTH)

solution["schedule"].create_csv()

visualisation(solution["schedule"])




# schedule = Schedule(csvdata("data/ConnectiesHolland.csv", "data/StationsNationaal.csv"), MIN_120)
# traject = Traject()
# traject.add(schedule.all_connections[1])
# traject.add(schedule.all_connections[0])
# traject.add(schedule.all_connections[27])
# traject.add(schedule.all_connections[6])
# traject.add(schedule.all_connections[4])
# traject.add(schedule.all_connections[3])
# traject.add(schedule.all_connections[2])
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[14])
# traject.add(schedule.all_connections[22])
# traject.add(schedule.all_connections[24])
# traject.add(schedule.all_connections[11])
# traject.add(schedule.all_connections[13])
# traject.add(schedule.all_connections[19])
# traject.add(schedule.all_connections[15])
# traject.add(schedule.all_connections[21])
# traject.add(schedule.all_connections[23])
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[20])
# traject.add(schedule.all_connections[8])
# traject.add(schedule.all_connections[7])
# traject.add(schedule.all_connections[5])
# traject.add(schedule.all_connections[16])
# traject.add(schedule.all_connections[26])
# traject.add(schedule.all_connections[25])
# traject.add(schedule.all_connections[10])
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[12])
# schedule.trajects.append(traject)
#
#
# traject = Traject()
# traject.add(schedule.all_connections[18])
# traject.add(schedule.all_connections[17])
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[9])
# schedule.trajects.append(traject)
#
# from newnew import Optimize
#
# optimize = Optimize(schedule, 4)
# optimize.run()
#
# # optimize(schedule)
# #
# visualisation(schedule.trajects, schedule.quality())

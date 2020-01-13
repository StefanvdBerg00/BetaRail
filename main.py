import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from visualisation import visualisation
from classes import City, Connection, Schedule, Traject
from csvdata import csvdata
from approach import approach
from new import optimize

def run(connections_file, coordinates_file, N, max_time, method, improve):
    best = {"schedule": None, "K": 0}

    print(f"{N}x {method}")
    for i in range(N):
        if N >= 100 and i % (N // 100) == 0:
            print(f"{(i // (N // 100))}%", end="\r")

        schedule = Schedule(csvdata(connections_file, coordinates_file), max_time)
        approach(schedule, method)

        if improve:
            optimize(schedule)

        quality = schedule.quality()

        if quality["K"] > best["K"]:
            best["schedule"] = schedule
            best["K"] = quality["K"]

    return best


MIN_180 = 180
MIN_120 = 120

N = 1000

A = "random"
B = "centered"
C = "outer"
D = "overlay"
E = "new"

IMPROVE = True

# schedule = Schedule(csvdata("data/ConnectiesHolland.csv", "data/StationsNationaal.csv"), MIN_120)
# traject = Traject()
# traject.add(schedule.all_connections[1])
# traject.add(schedule.all_connections[0])
# traject.add(schedule.all_connections[27])
# traject.add(schedule.all_connections[6])
# traject.add(schedule.all_connections[4])
# traject.add(schedule.all_connections[3])
# traject.add(schedule.all_connections[2])
# traject.route = [schedule.cities["Den Helder"], schedule.cities["Alkmaar"], schedule.cities["Hoorn"], schedule.cities["Zaandam"], schedule.cities["Amsterdam Sloterdijk"], schedule.cities["Amsterdam Centraal"], schedule.cities["Amsterdam Amstel"], schedule.cities["Amsterdam Zuid"]]
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
# traject.route = [schedule.cities["Dordrecht"], schedule.cities["Rotterdam Centraal"], schedule.cities["Schiedam Centrum"], schedule.cities["Delft"], schedule.cities["Den Haag Centraal"], schedule.cities["Leiden Centraal"], schedule.cities["Alphen a/d Rijn"], schedule.cities["Gouda"], schedule.cities["Rotterdam Alexander"], schedule.cities["Rotterdam Centraal"]]
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
# traject.route = [schedule.cities["Leiden Centraal"], schedule.cities["Schiphol Airport"], schedule.cities["Amsterdam Zuid"], schedule.cities["Amsterdam Sloterdijk"], schedule.cities["Haarlem"], schedule.cities["Beverwijk"], schedule.cities["Zaandam"], schedule.cities["Castricum"], schedule.cities["Alkmaar"]]
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[12])
# traject.route = [schedule.cities["Gouda"], schedule.cities["Den Haag Centraal"]]
# schedule.trajects.append(traject)
#
#
# traject = Traject()
# traject.add(schedule.all_connections[18])
# traject.add(schedule.all_connections[17])
# traject.route = [schedule.cities["Leiden Centraal"], schedule.cities["Heemstede-Aerdenhout"], schedule.cities["Haarlem"]]
# schedule.trajects.append(traject)
#
# traject = Traject()
# traject.add(schedule.all_connections[9])
# traject.route = [schedule.cities["Beverwijk"], schedule.cities["Castricum"]]
# schedule.trajects.append(traject)
#
# optimize(schedule)
#
# visualisation(schedule.trajects, schedule.quality())


# for connection in schedule.all_connections:
#     traject = Traject()
#     traject.add(connection)
#     traject.route = [connection.city1, connection.city1.new_current(connection)]
#     schedule.trajects.append(traject)
# optimize(schedule)
# visualisation(schedule.trajects, schedule.quality())


solution = run("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv", N, MIN_180, E, IMPROVE)

solution["schedule"].create_csv()

visualisation(solution["schedule"].trajects, solution["schedule"].quality())

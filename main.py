# ****************************************************************************
# main.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from output import run, dump, load
from visualisation import visualisation
from heuristic import Heuristic

# Maximum time of a traject
MIN_180 = 180
MIN_120 = 120

# Amount of iterations
N = 100

# Algorithm specifications
IMPROVE = True
DEPTH = 4
FILTER = ""

# Starting in random city, choosing random connections
A = Heuristic("random", Heuristic.random_city, Heuristic.general_connections)

# Starting in city with most connections, choosing random connections
B = Heuristic("centered", Heuristic.centered_city, Heuristic.general_connections)

# Starting in city with least connections, choosing random connections
C = Heuristic("outer", Heuristic.outer_city, Heuristic.general_connections)

# Starting in random city, choosing connections based on probability distribution
D = Heuristic("overlay", Heuristic.random_city, Heuristic.overlay_connections)

# Starting in random city, continuing to city with least connections
E = Heuristic("new", Heuristic.random_city, Heuristic.new_connections)

solution = run("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv", N, MIN_180, A, IMPROVE, DEPTH, FILTER)

# Save best solution
dump(solution["schedule"])

# Save solution in solution.csv
solution["schedule"].create_csv()

visualisation(solution["schedule"])

# visualisation(load())





# # data
# import csv
# for method in [B]:
#     for n in range(3, 4):
#         print(n)
#         solution = run("data/ConnectiesNationaal.csv", "data/StationsNationaal.csv", 1*10**n, MIN_180, method, IMPROVE, DEPTH, FILTER)
#         K_all = [x["K"] for x in solution["All"]]
#         K_max = max(K_all)
#         K_min = min(K_all)
#         K_avg = sum(K_all)/len(K_all)
#
#         with open('results/data7.csv', mode="a", newline="") as file:
#             writer = csv.writer(file, delimiter=",")
#             writer.writerow([method.name, solution["schedule"].quality(), len(K_all), True, K_min, K_avg, K_max])

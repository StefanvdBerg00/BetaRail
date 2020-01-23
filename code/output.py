# ****************************************************************************
# output.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import pickle
from classes import Schedule
from csvdata import csvdata
from optimize import Optimize
from visualisation import visualisation

def run(connections_file, coordinates_file, file_name, N, max_time, method, improve, depth, exclusion):
    """ Runs algorithm with specified heuristic and returns best schedule. """

    best = {"schedule": None, "K": 0, "All": []}

    print(f"{N}x {method.name}")

    for i in range(N):

        # Display progress
        if N >= 100 and i % (N // 100) == 0:
            print(f"{(i // (N // 100))}%", end="\r")

        method.schedule = Schedule(csvdata(connections_file, coordinates_file, exclusion), max_time)
        method.run()

        if improve:
            optimize = Optimize(method.schedule, depth)
            optimize.run()

        quality = method.schedule.quality()
        best["All"].append(quality)

        # Keep track of best schedule
        if quality["K"] > best["K"]:
            best["schedule"] = method.schedule
            best["K"] = quality["K"]

    dump(best["schedule"], file_name)
    best["schedule"].create_csv()
    print(best["K"])
    # visualisation(best["schedule"])

def dump(schedule, file_name):
    """ Checks if given schedule is better than best schedule. """

    try:
        best = load(file_name)

        if schedule.quality()["K"] > best.quality()["K"]:
            with open(f"results/{file_name}", "wb") as file:
                pickle.dump(schedule, file)
    except:
        with open(f"results/{file_name}", "wb") as file:
            pickle.dump(schedule, file)

def load(file_name):
    """ Loads best schedule so far. """

    with open(f"results/{file_name}", "rb") as file:
        return pickle.load(file)

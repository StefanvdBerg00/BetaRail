import pickle
from classes import Schedule
from csvdata import csvdata
from optimize import Optimize

def run(connections_file, coordinates_file, N, max_time, method, improve, depth, filter):
    """ Runs algorithm with specified heuristic and returns best schedule. """

    best = {"schedule": None, "K": 0, "All": []}

    print(f"{N}x {method.name}")

    for i in range(N):

        # Display progress
        if N >= 100 and i % (N // 100) == 0:
            print(f"{(i // (N // 100))}%", end="\r")

        method.schedule = Schedule(csvdata(connections_file, coordinates_file, filter), max_time)
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

    return best

def dump(schedule):
    """ Checks if given schedule is better than best schedule. """

    try:
        best = load()

        if schedule.quality()["K"] > best.quality()["K"]:
            with open("results/Nederland", "wb") as file:
                pickle.dump(schedule, file)
    except:
        with open("results/Nederland", "wb") as file:
            pickle.dump(schedule, file)

def load():
    """ Loads best schedule so far. """

    with open("results/Nederland", "rb") as file:
        return pickle.load(file)

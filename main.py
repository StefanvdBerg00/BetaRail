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
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "input"))
sys.path.append(os.path.join(directory, "code", "output"))

from output import run, load
from visualisation import visualisation
from heuristic import Heuristic

CONNECTIONS_FILE = "data/ConnectiesNationaal.csv"
COORDINATES_FILE = "data/StationsNationaal.csv"
BEST_SCHEDULE_FILE = "results/Nederland"

# CONNECTIONS_FILE = "data/ConnectiesHolland.csv"
# COORDINATES_FILE = "data/StationsNationaal.csv"
# BEST_SCHEDULE_FILE = "results/Holland"

# Amount of iterations
N = 100

# Maximum time of a traject
MIN_180 = 180
MIN_120 = 120

# Improve algorithm on/off
IMPROVE = True
DEPTH = 4

# Name of city to exclude from schedule
EXCLUSION = ""


# Starting in random city, choosing random connections
A = Heuristic("random", Heuristic.random_city, Heuristic.general_connections)

# Starting in city with most connections, choosing random connections
B = Heuristic("centered", Heuristic.centered_city, Heuristic.general_connections)

# Starting in city with least connections, choosing random connections
C = Heuristic("outer", Heuristic.outer_city, Heuristic.general_connections)

# Starting in random city, choosing connections based on probability distribution
D = Heuristic("overlay", Heuristic.random_city, Heuristic.overlay_connections)

# Starting in random city, continuing to city with least connections
E = Heuristic("lookahead", Heuristic.random_city, Heuristic.least_connections)

run(CONNECTIONS_FILE, COORDINATES_FILE, BEST_SCHEDULE_FILE, N, MIN_180, IMPROVE, DEPTH, EXCLUSION, C)

# visualisation(load(BEST_SCHEDULE_FILE))

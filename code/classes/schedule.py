# ****************************************************************************
# schedule.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ***************************************************************************/

import csv


class Schedule:
    def __init__(self, data, max_time):
        self.trajects = []
        self.all_connections = data["all_connections"]
        self.number_connections = len(self.all_connections)
        self.cities = data["cities"]
        self.max_time = max_time

    def get_trajects(self):
        """ Returns all trajects in schedule. """
        return self.trajects

    def get_all_connections(self):
        """ Returns all possible connections in schedule. """
        return self.all_connections

    def get_cities(self):
        """ Returns all cities in schedule. """
        return self.cities

    def get_max_time(self):
        """ Returns the maximum time of a traject. """
        return self.max_time

    def add_traject(self, traject):
        """ Adds a traject to schedule. """
        self.trajects.append(traject)

    def quality(self):
        """ Returns the quality of schedule. """
        T = len(self.trajects)
        Min = sum([traject.get_time() for traject in self.trajects])
        connections = []
        [connections.extend(connection) for connection in [traject.get_connections() \
        for traject in self.trajects]]
        p = len(set(connections)) / self.number_connections

        return {"p": p, "T": T, "Min": Min, "K": p*10000 - (T*100 + Min)}

    def create_csv(self):
        """ Creates a csv-file for schedule. """
        with open('results/solution.csv', mode="w", newline="") as solution_file:
            solution_writer = csv.writer(solution_file, delimiter=",")
            solution_writer.writerow(["trein", "lijnvoering"])

            for i, traject in enumerate(self.trajects):
                solution_writer.writerow([f"trein_{i + 1}", traject.get_route()])

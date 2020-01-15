import copy
from classes import Traject

class Optimize:
    def __init__(self, schedule, depth):
        self.stack = []
        self.traject = None
        self.schedule = schedule
        self.depth = depth
        self.shortest = {"time": 0}

    def run(self):
        while self.shortest["time"] != 100:
            self.shortest = {"time": 100, "state": None, "old_trajects": []}

            for traject in self.schedule.trajects:
                self.traject = traject
                self.DepthFirst(traject.route[0])
                self.DepthFirst(traject.route[-1])

            if self.shortest["state"]:
                self.shortest["state"].time = self.shortest["state"].time + self.shortest["old_trajects"][1].time
                if self.shortest["state"].current_city == self.shortest["old_trajects"][1].route[0]:
                    self.shortest["state"].connections += self.shortest["old_trajects"][1].connections
                    self.shortest["state"].route += self.shortest["old_trajects"][1].route[1:]
                else:
                    self.shortest["state"].connections = self.shortest["old_trajects"][1].connections + self.shortest["state"].connections
                    self.shortest["state"].route = self.shortest["old_trajects"][1].route + self.shortest["state"].route[1:]

                self.schedule.trajects.remove(self.shortest["old_trajects"][0])
                self.schedule.trajects.remove(self.shortest["old_trajects"][1])
                self.schedule.trajects.append(self.shortest["state"])

    def DepthFirst(self, city):
        self.stack.append(self.traject)
        self.stack[0].current_city = city

        while len(self.stack) > 0:
            state = self.stack.pop()

            for traject in [traject for traject in self.schedule.trajects if traject != self.traject]:
                if state.time - self.traject.time < self.shortest["time"] and traject.time + state.time < self.schedule.max_time and traject.can_connect(state):
                    self.shortest = {"time": state.time - self.traject.time, "state": state, "old_trajects": [self.traject, traject]}

            if len(state.connections) - len(self.traject.connections) < self.depth and state.time - self.traject.time < self.shortest["time"]:
                for connection in [connection for connection in state.current_city.connections if connection not in state.connections]:
                    traject = copy.deepcopy(state)
                    traject.add(connection)
                    traject.current_city  = state.current_city.new_current(connection)
                    traject.route.append(traject.current_city)
                    self.stack.append(traject)

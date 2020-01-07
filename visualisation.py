import matplotlib.pyplot as plt
import csv

def visualisation(connections):
    for connection in connections:
        plt.plot([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x])
        plt.annotate(connection.city1.name, (connection.city1.y, connection.city1.x))
        plt.annotate(connection.city2.name, (connection.city2.y, connection.city2.x))
        plt.scatter([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x])

    plt.show()

import matplotlib.pyplot as plt
import mplcursors
import csv

def visualisation(connections, quality):
    plt.imshow(plt.imread("map1.png"), extent=[3.315, 7.222, 50.703, 53.622])
    data = []

    for connection in connections:
        plt.plot([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x], "red", zorder=1)
        data.append(plt.scatter(connection.city1.y, connection.city1.x, color="blue", zorder=2, label=connection.city1.name))
        data.append(plt.scatter(connection.city2.y, connection.city2.x, color="blue", zorder=2, label=connection.city2.name))

    text = "K:     " + str(quality["K"]) + "\np:     " + str(quality["p"]) + "\nT:     " + str(quality["T"]) + "\nMin: " + str(quality["Min"])

    plt.text(3.5, 52.95, text, bbox=dict(facecolor='beige', edgecolor='black'))
    plt.xlim(3.355, 7.222)
    plt.ylim(50.703, 53.522)
    mplcursors.cursor(data, hover=True)
    plt.show()

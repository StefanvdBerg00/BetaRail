import matplotlib
import matplotlib.pyplot as plt
import mplcursors
import csv
from random import randrange

def visualisation(trajects, quality):

    plt.imshow(plt.imread("map1.png"), extent=[3.315, 7.222, 50.703, 53.622])
    data = []

    colors = [hex for name, hex in matplotlib.colors.cnames.items()]

    for traject in trajects:
        i = randrange(len(colors))
        
        for connection in traject["route"]:
            plt.plot([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x], color=colors[i], zorder=1)

            data.append(plt.scatter(connection.city1.y, connection.city1.x, color="blue", zorder=2, label=connection.city1.name))
            data.append(plt.scatter(connection.city2.y, connection.city2.x, color="blue", zorder=2, label=connection.city2.name))

    text = "K:     " + str(quality["K"]) + "\np:     " + str(quality["p"]) + "\nT:     " + str(quality["T"]) + "\nMin: " + str(quality["Min"])

    plt.text(3.5, 52.95, text, bbox=dict(facecolor='beige', edgecolor='black'))
    plt.xlim(3.355, 7.222)
    plt.ylim(50.703, 53.522)
    mplcursors.cursor(data, hover=True)
    plt.show()

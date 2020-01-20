import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import mplcursors
import csv
import random

def visualisation(schedule):
    trajects = schedule.get_trajects()
    color = 0
    color_step = 1 / len(trajects) if len(trajects) != 0 else 0

    fig, ax = plt.subplots()
    plt.imshow(plt.imread("map1.png"), extent=[3.315, 7.222, 50.703, 53.622])
    points = []
    lines = {}

    for i, traject in enumerate(trajects):
        route = traject.get_route()
        label = f"{route[0]} -- {traject.get_time()} -> {route[-1]}"
        lines[label] = []
        color += color_step

        for connection in traject.connections:
            lines[label].append(ax.plot([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x], visible=False, label=label, color=matplotlib.colors.hsv_to_rgb([color, 1, 1]), zorder=2))

            ax.plot([connection.city1.y, connection.city2.y], [connection.city1.x, connection.city2.x], color="lightgrey", zorder=1)
            points.append(ax.scatter(connection.city1.y, connection.city1.x, color="blue", zorder=3, label=connection.city1.name))
            points.append(ax.scatter(connection.city2.y, connection.city2.x, color="blue", zorder=3, label=connection.city2.name))

    quality = schedule.quality()
    text = "K:     " + str(quality["K"]) + "\np:     " + str(quality["p"]) + "\nT:     " + str(quality["T"]) + "\nMin: " + str(quality["Min"])

    plt.subplots_adjust(left=0.4)
    check = CheckButtons(plt.axes([0.01, 0, 0.30, 1.0]), lines.keys())

    def func(label):
        for line in lines[label]:
            line[0].set_visible(not line[0].get_visible())
        plt.draw()

    check.on_clicked(func)

    ax.text(3.5, 52.95, text, bbox=dict(facecolor='#ffff7f', edgecolor='black'))
    plt.xlim(3.355, 7.222)
    plt.ylim(50.703, 53.522)
    mplcursors.cursor(points, hover=True).connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
    plt.show()

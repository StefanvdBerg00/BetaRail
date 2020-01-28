# ****************************************************************************
# visualisation.py
#
# RailNL - Team BetaRail
# Amber Remmelzwaal, Ilse de Langen & Stefan van den Berg
#
# Programmeertheorie
# ****************************************************************************

import matplotlib, mplcursors, csv, random
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

def visualisation(schedule):
    """ Visualises schedule on the map. """

    trajects = schedule.get_trajects()

    # Divide the color spectrum in the number of trajects
    color = 0
    color_step = 1 / len(trajects) if len(trajects) != 0 else 0

    fig, ax = plt.subplots()
    plt.imshow(plt.imread("images/map.png"), extent=[3.315, 7.222, 50.703, 53.622])
    points = []
    lines = {}

    connections = []
    [connections.extend(connection) for connection in \
    [traject.get_connections() for traject in schedule.get_trajects()]]

    for connection in schedule.get_all_connections():

        # Plot every connection in lightgrey
        ax.plot([connection.city1.get_y(), connection.city2.get_y()],
                [connection.city1.get_x(), connection.city2.get_x()],
                color="lightgrey", zorder=1)

        # Remember every city
        points.append(ax.scatter(connection.city1.get_y(), connection.city1.get_x(),
                                 color="blue", zorder=3, label=connection.city1.get_name()))

        points.append(ax.scatter(connection.city2.get_y(), connection.city2.get_x(),
                                 color="blue", zorder=3, label=connection.city2.get_name()))

        # Plot red dashed line when connection is removed from schedule
        if connection not in connections:
            ax.plot([connection.city1.get_y(), connection.city2.get_y()],
                    [connection.city1.get_x(), connection.city2.get_x()],
                    "r--", zorder=1)

    for i, traject in enumerate(trajects):
        route = traject.get_route()
        label = f"{route[0].get_name()} -> {route[-1].get_name()} ({traject.get_time()})"
        lines[label] = []
        color += color_step

        for connection in traject.connections:

            # Remember every line with its own color for the legend
            lines[label].append(ax.plot([connection.city1.get_y(), connection.city2.get_y()],
                                        [connection.city1.get_x(), connection.city2.get_x()],
                                        visible=False, label=label,
                                        color=matplotlib.colors.hsv_to_rgb([color, 1, 1]), zorder=2))

    # For showing the score
    quality = schedule.quality()
    text = "K:     " + str(quality["K"]) + "\np:     " + str(quality["p"]) + "\nT:     " \
            + str(quality["T"]) + "\nMin: " + str(quality["Min"])

    plt.subplots_adjust(left=0.4)
    check = CheckButtons(plt.axes([0.01, 0, 0.30, 1.0]), lines.keys())

    def func(label):
        """ Switches a traject on or off. """
        for line in lines[label]:
            line[0].set_visible(not line[0].get_visible())
        plt.draw()

    check.on_clicked(func)

    ax.text(3.5, 52.95, text, bbox=dict(facecolor='#ffff7f', edgecolor='black'))
    plt.xlim(3.355, 7.222)
    plt.ylim(50.703, 53.522)

    # Let city appear when hover
    mplcursors.cursor(points, hover=True).connect("add",
    lambda sel: sel.annotation.set_text(sel.artist.get_label()))
    plt.show()

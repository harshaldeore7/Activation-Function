import numpy as np
import matplotlib.pyplot as plt


def ReLu(inputs):
    ReLu_scores = [max(0, x) for x in inputs]
    return ReLu_scores


def line_graph(x, y, x_title, y_title):
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


graph_x = range(-21, 21)
graph_y = ReLu(graph_x)

print("Graph X readings: {}".format(graph_x))
print("Graph Y readings: {}".format(graph_y))

line_graph(graph_x, graph_y, "Inputs", "ReLu Scores")

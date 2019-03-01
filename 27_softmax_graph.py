import numpy as np
import matplotlib.pyplot as plt


def softmax(inputs):
    return np.exp(inputs) / float(sum(np.exp(inputs)))


def line_graph(x, y, x_title, y_title):
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


graph_x = range(-21, 21)
graph_y = softmax(graph_x)

print("Graph X readings: {}".format(graph_x))
print("Graph Y readings: {}".format(graph_y))

line_graph(graph_x, graph_y, "Inputs", "Softmax Scores")

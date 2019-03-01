import math

global x1, x2, b, w, sum1
x1 = [2, -3, 1]
x2 = [6, 7, -3]
b = [1, 1, 1]
w = [0.5, 0.7, 1]
sum1 = [0, 0, 0]


def summation():
    tsum = 0
    for i in range(0, 3):
        sum1[i] = (x1[i] * w[i]) + (x2[i] * w[i]) + (b[i] * w[i])
        tsum += sum1[i]
    return tsum


def sigmoid(x):
    sigmoid_scores = [1 / float(1 + math.exp(- x))]
    return sigmoid_scores


sum_1 = summation()
output = sigmoid(sum_1)
print("Sigmoid Function Output :: {}".format(output))

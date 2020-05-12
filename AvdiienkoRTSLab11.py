import math
import random

from datetime import datetime

import matplotlib.pyplot as plt


def signal_analyze(waves, marks):

    amplitude = random.uniform(0, 1)
    phi = random.uniform(0, 1)

    Y = [sum([signal(i, (j * marks) / waves, amplitude, phi) for j in range(waves)]) for i in range(marks)]
    arguments = [i for i in range(marks)]
    expected_value = sum(Y, marks) / marks
    dispersion = sum([pow((i - expected_value), 2) for i in Y]) / marks - 1

    return dispersion, arguments, Y,


def signal(t, w, ampl, phi):
    return math.sin(w * t + phi) * ampl


if __name__ == '__main__':
    variant = 7101
    Ω = 1200                            # cutoff frequency
    n = 6                               # number of sine waves
    N = 64                              # number of discrete marks

    exec_start = datetime.now()
    my_dispersion, argument_x_axis, function_y_axis = signal_analyze(n, N)
    exec_finish = datetime.now()
    print(f"Total execution time: {exec_finish - exec_start}ms.")

    plt.ylabel("x(t) = A*sin(t * \u03a9 + \u03c6)")
    plt.xlabel(f"x(t)")
    plt.plot(argument_x_axis, function_y_axis)
    plt.show()

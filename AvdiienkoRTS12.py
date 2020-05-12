import random
import matplotlib.pyplot as plt

from datetime import datetime

import AvdiienkoRTSLab11 as Lab1


def second_signal_analyze(waves, marks, function1_y_axis):

    amplitude2 = random.uniform(0, 1)
    φ = random.uniform(0, 1)

    function2_y_axis = [sum([Lab1.signal(i, (j * waves) / marks, amplitude2, φ) for j in range(marks)]) for i in range(waves)]

    function1_half_y_axis = function1_y_axis[:len(function1_y_axis) // 2]
    function2_half_y_axis = function2_y_axis[:len(function2_y_axis) // 2]

    expected_value1 = sum(function1_y_axis, marks) / marks
    expected_value2 = sum(function2_y_axis, marks) / marks

    dispersion1 = sum([pow((i - expected_value1), 2) for i in Y]) / marks - 1
    dispersion2 = sum([pow((i - expected_value2), 2) for i in Y]) / marks - 1

    correlation_y1_axis = [correlation(function1_half_y_axis, function1_y_axis[i: i + waves // 2],
                                       expected_value1, waves // 2) for i in range(waves // 2)]

    correlation_y2_axis = [correlation(function2_half_y_axis, function2_y_axis[i: i + waves // 2],
                                       expected_value2, waves // 2) for i in range(waves // 2)]

    correlation_y1_axis = [value / dispersion1 for value in correlation_y1_axis]
    correlation_y2_axis = [value / dispersion2 for value in correlation_y2_axis]

    return correlation_y1_axis, correlation_y2_axis


def correlation(t_arr, tau_arr, mx, number):
    return sum(((t_arr[i] - mx)*(tau_arr[i] - mx)) for i in range(number)) / (number - 1)


if __name__ == '__main__':
    Ω = 1200  # cutoff frequency
    n = 6  # number of sine waves
    N = 64  # number of discrete marks

    my_dispersion, first_func_X, first_func_Y = Lab1.first_signal_analyze(n, N)
    X = first_func_X
    Y = first_func_Y

    exec_start = datetime.now()
    first_correlation, second_correlation = second_signal_analyze(n, N, Y)
    exec_finish = datetime.now()
    print(f"Time of execution = {exec_start - exec_finish}")

    plt.subplot(2, 1, 1)
    plt.ylabel("R(xx)")
    plt.plot([i for i in range(n // 2)], first_correlation)
    plt.subplot(2, 1, 2)
    plt.ylabel("R(xy)")
    plt.plot([i for i in range(n // 2)], second_correlation)
    plt.show()

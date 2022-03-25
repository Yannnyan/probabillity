import math

import distributions
from generator import *
from Distribution_Properties import *


def generate_centerPoints(jump: int, r: int):
    if jump <= 0 or r <= 0:
        return
    l = []
    for i in range(jump, r, jump):
        l.append(i)
    return l


def generate_intervals(inc: int, r: int):
    if inc <= 0 or r <= 0:
        return
    l = []
    for i in range(1, r, inc):
        l.append(i)
    return l


def markov_inequality(expec, t):
    """
        given expectation and a variable t calculate upper bound for a random variable to appear larger than the expectation.
        return the upper bound for the probability for the to happen.
    """
    if t == 0:
        return 0
    return expec / t


def chebyshev_inequality(variance, t):
    """
    Given Variance of a random variable and parameter t, calculate the probabillity for the random
    variable to appear inside the interval (Expectation - t, Expectation + t).
    :return:
    """
    if t == 0:
        return 0
    if variance < 0:
        return 0
    return 1 - (variance / math.pow(t, 2))


def output_markov(points, expec):
    l = {}
    for t in points:
        l[t] = (markov_inequality(expec, t))
    return l


def output_chebyshev(intervals, variance):
    l = {}
    for t in intervals:
        l[t] = (chebyshev_inequality(variance, t))
    return l


def output_string(name: str, result, point=0, interval=0, expec= 0):
    if name == "markov":
        return "The probabillity for the random variable to be bigger than or equal to " + str(point) + " is " + str(result)
    elif name == "chebyshev":
        return "The probabillity for the random variable to be inside the interval [ " + str(expec - interval) + "," + str(expec + interval) + " ] is " + str(result)


def main():
    expec = calc_expectation(name="Binom", n=100, p=0.3)
    variance = calc_Variance("Binom", n=100, p=0.3)
    points = generate_centerPoints(5, 100)
    intervals = generate_intervals(1, 100)
    print("expectation is " + str(expec))
    markov = output_markov(points=points, expec=expec)
    for p in markov.keys():
        print(output_string(name="markov", point=p, result=markov[p]))
    print("variance is " + str(variance))
    chebyshev = output_chebyshev(intervals=intervals, variance=variance)
    for interval in chebyshev.keys():
        print(output_string(name="chebyshev", interval=interval, result=chebyshev[interval], expec= expec))


if __name__ == "__main__":
    main()

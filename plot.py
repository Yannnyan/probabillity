import random
import sys

import matplotlib.pylab as plt

from generator import *

number_of_tries = 100000
size_sample_space = 100
probabilities = {}
successes = {}
values = []

plt.xlabel('Value of the random variable ')


def plot_binom(N=100, p=0.7777):
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="binom", values=values, N=N, p=p)
    plt.title("Binominal distribution with N= " + str(N) + " with probabillity " + str(p))
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def plot_poisson(gamma=0.6):
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="poisson", values=values, gamma=gamma)
    plt.title("Poisson distribution with gamma= " + str(gamma))
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def plot_uniform():
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="uni", values=values)
    plt.title("Uniform distribution ")
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def plot_bernolli(p=0.7):
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="bernolli", p=p, values=values)
    plt.title("Bernoulli distribution with probabillity " + str(p))
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def plot_geom(p=5):
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="geom", p=p, values=values)
    plt.title("Geometric distribution with probabillity " + str(p))
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def plot_hypGeom(N=100, D=50, n=40):
    global number_of_tries, probabilities, successes
    probabilities = generate_probabilities(dist="hyp", values=values, N=N, D=D, n=n)
    plt.title("HyperGeometric distribution with N= " + str(N) + " D= " + str(D) + " n= " + str(n))
    successes = generate_successes(n=number_of_tries, values=values, probabilities= probabilities)


def main():
    global size_sample_space, successes, values
    args = sys.argv[1:]
    values = generate_values(n= size_sample_space)
    # plot_uniform()
    # plot_geom()
    plot_hypGeom()
    # plot_binom()
    # plot_bernolli()
    # plot_poisson(gamma= 5)
    suc = list(successes.values())
    print(values)
    print(list(probabilities.values()))
    print(suc)
    plt.plot(values, suc)

    plt.ylabel('Amount of successfull tries (out of ' + str(number_of_tries) + ')')
    plt.show()


if __name__ == '__main__':
    main()

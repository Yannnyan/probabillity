import random
import sys

import matplotlib.pylab as plt

import distributions

number_of_tries = 100000
size_sample_space = 100
probabilities = {}
successes = {}
values = []

plt.xlabel('Value of the random variable ')


def generate_values(n):
    global values
    values = []
    for i in range(n):
        values.append(i)
        successes[i] = 0
    return values


def generate_probabilities(dist, N=0, D=0, n=0, p=0.0, gamma=0.0):
    global probabilities
    probabilities = {}
    if dist == "poisson":
        for value in values:
            probabilities[value] = (distributions.poisson_distribution(gamma, value))
    elif dist == "geom":
        for value in values:
            probabilities[value] = (distributions.geometric_distribution(value, p))
    elif dist == "binom":
        for value in values:
            probabilities[value] = (distributions.binominal_distribution(N, p, value))
    elif dist == "uni":
        for value in values:
            probabilities[value] = (distributions.uniform_distribution(len(values)))
    elif dist == "hyp":
        for value in values:
            probabilities[value] = (distributions.hypGeom_distrubituion(N, D, n, value))
    elif dist == "bernolli":
        for value in values:
            probabilities[value] = (distributions.bernulli_distribution(p, value))


# n is the number of samples for each value
def generate_successes(n: int):
    global successes
    for value in values:
        p = probabilities[value]
        for i in range(n):
            x = random.random() * 100
            if x <= p * 100:
                successes[value] += 1


def plot_binom(N=100, p=0.7777):
    global number_of_tries
    generate_probabilities("binom", N=N, p=p)
    plt.title("Binominal distribution with N= " + str(N) + " with probabillity " + str(p))
    generate_successes(number_of_tries)


def plot_poisson(gamma=0.6):
    global number_of_tries
    generate_probabilities("poisson", gamma=gamma)
    plt.title("Poisson distribution with gamma= " + str(gamma))
    generate_successes(number_of_tries)


def plot_uniform():
    global number_of_tries
    generate_probabilities("uni")
    plt.title("Uniform distribution ")
    generate_successes(number_of_tries)


def plot_bernolli(p=0.7):
    global number_of_tries
    generate_probabilities("bernolli", p=p)
    plt.title("Bernoulli distribution with probabillity " + str(p))
    generate_successes(number_of_tries)


def plot_geom(p=0.5):
    global number_of_tries
    generate_probabilities("geom", p=p)
    plt.title("Geometric distribution with probabillity " + str(p))
    generate_successes(number_of_tries)


def plot_hypGeom(N=100, D=50, n=40):
    global number_of_tries
    generate_probabilities("hyp", N=N, D=D, n=n)
    plt.title("HyperGeometric distribution with N= " + str(N) + " D= " + str(D) + " n= " + str(n))
    generate_successes(number_of_tries)


def main():
    global size_sample_space
    args = sys.argv[1:]
    generate_values(size_sample_space)
    # plot_uniform()
    # plot_geom()
    # plot_hypGeom()
    plot_binom()
    # plot_bernolli()
    # plot_poisson()
    suc = list(successes.values())
    print(values)
    print(list(probabilities.values()))
    print(suc)
    plt.plot(values, suc)

    plt.ylabel('Amount of successfull tries (out of ' + str(number_of_tries) + ')')
    plt.show()


if __name__ == '__main__':
    main()

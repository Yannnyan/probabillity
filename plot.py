import random
import sys

import matplotlib.pylab as plt

import distributions

probabilities = {}
successes = {}
values = []


plt.xlabel('Value of the random variable ')
plt.ylabel('Amount of successfull tries (out of 100000)')


def generate_values(n):
    global values
    values = []
    for i in range(n):
        values.append(i)
        successes[i] = 0
    return values


def generate_probabilities(dist, N=0, D=0, n=0, p=0, gamma=0.0):
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


def main():
    args = sys.argv[1:]
    generate_values(100)
    # generate_probabilities("hyp", N= 100, D= 50, n= 40)
    # generate_probabilities("binom", N= 100, p= 0.7777)
    # generate_probabilities("poisson", gamma= 0.6)
    # generate_probabilities("poisson",gamma= 20)
    # generate_probabilities("uni")
    # generate_probabilities("geom", p= 0.5)
    generate_probabilities("bernolli" , p = 0.7)
    generate_successes(100000)
    suc =  list(successes.values())
    print(values)
    print(list(probabilities.values()))
    print(suc)
    plt.plot(values, suc)
    plt.show()

if __name__ == '__main__':
    main()



import distributions
import random


def generate_values(n):
    values = []
    for i in range(n):
        values.append(i)
    return values


def generate_probabilities(dist, values, N=0, D=0, n=0, p=0.0, gamma=0.0):
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
    return probabilities


# n is the number of samples for each value
def generate_successes(n: int, values: [], probabilities: dict) -> {}:
    successes = {}
    for value in values:
        successes[value] = 0
        p = probabilities[value]
        for i in range(n):
            x = random.random() * 100
            if x <= p * 100:
                successes[value] += 1
    return successes

import math


def binominal_distribution(N, p, k):
    if k > N:
        return 0
    if p < 0 or p > 1:
        return 0
    return choose(N, k) * math.pow(p, k) * math.pow(1 - p, N - k)


def poisson_distribution(gamma, k):
    if gamma <= 0:
        return 0
    return math.pow(math.e, -gamma) * math.pow(gamma, k) / factorial(k)


def geometric_distribution(k, p):
    if p < 0 or p > 1:
        return 0
    if k <= 0:
        return 0
    return p * math.pow(1 - p, k - 1)


def uniform_distribution(n):
    if n <= 0:
        return 0
    return 1 / n


def hypGeom_distrubituion(N, D, n, k) -> []:
    ret = choose(D, k) * choose(N - D, n - k) / choose(N, n)
    return ret


def bernulli_distribution(p, x):
    if x == 1:
        return p
    elif x == 0:
        return 1 - p
    else:
        return 0


def NB_distribution(self, N):
    pass


def factorial(k: int):
    if k < 0:
        return -1
    ret = 1
    for i in range(1, k + 1, 1):
        ret *= i
    return ret


def choose(n: int, k: int):
    if k > n:
        return 0
    if k < 0:
        return -1
    ret = factorial(n) / (factorial(k) * factorial(n - k))
    return ret

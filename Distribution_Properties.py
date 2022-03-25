
def calc_Variance(name: str, n= 0, p= 0, N= 0, gamma= 0, D = 0):
    """
    Binom, NB, Poisson, Geom, Bernoulli, hypGeom

    :param name:
    :param n:
    :param p:
    :param N:
    :param gamma:
    :param D:
    :return:
    """
    if name == "Binom":
        return n * (p - p * p)
    elif name == "NB":
        pass
    elif name == "Poisson":
        return gamma * gamma
    elif name == "Geom":
        return (1 - p) / p * p
    elif name == "Bernoulli":
        return p
    elif name == "hypGeom":
        return n * D * (N - D) * (N - n) / (N * N * (N - 1))
    else:
        return 0


def calc_expectation(name: str, n= 0, p= 0, N= 0, gamma= 0, D = 0):
    """
      Binom, NB, Poisson, Geom, Bernoulli, hypGeom

      :param name:
      :param n:
      :param p:
      :param N:
      :param gamma:
      :param D:
      :return:
      """
    if name == "Binom":
        return n * p
    elif name == "NB":
        pass
    elif name == "Poisson":
        return gamma
    elif name == "Geom":
        return 1 / p
    elif name == "Bernoulli":
        return p
    elif name == "hypGeom":
        return n * D / N
    else:
        return 0

import random
from character import Character


def crossover(p1, p2, cross_alg):
    if cross_alg == 'one_point':
        return one_point(p1, p2)
    if cross_alg == 'two_point':
        return two_point(p1, p2)
    if cross_alg == 'uniform':
        return uniform(p1, p2)
    if cross_alg == 'anular':
        return anular(p1, p2)


def one_point(p1, p2):
    gen1 = p1.get_gen
    gen2 = p2.get_gen
    index_nr = min(len(gen1), len(gen2))
    n = random.randint(0, index_nr - 1)  # Index for one-point crossover
    child1 = gen1[:n] + gen2[n:]
    child2 = gen2[:n] + gen1[n:]

    return child1, child2


def two_point(p1, p2):
    gen1 = p1.get_gen
    gen2 = p2.get_gen

    index_nr = min(len(gen1), len(gen2))  # Calculate the maximum index for two-point crossover

    n1 = random.randint(0, index_nr - 2)  # Index for the first crossover point
    n2 = random.randint(n1 + 1, index_nr - 1)  # Index for the second crossover point

    child1 = gen1[:n1] + gen2[n1:n2] + gen1[n2:]
    child2 = gen2[:n1] + gen1[n1:n2] + gen2[n2:]

    return child1, child2


def uniform(p1, p2):
    gen1 = p1.get_gen
    gen2 = p2.get_gen

    index_nr = min(len(gen1), len(gen2))  # Calculate the maximum index for uniform crossover

    child1 = []
    child2 = []

    for i in range(index_nr):
        if random.random() < 0.5:  # Select gene from parent 1
            child1.append(gen1[i])
            child2.append(gen2[i])
        else:  # Select gene from parent 2
            child1.append(gen2[i])
            child2.append(gen1[i])

    child1 = ''.join(child1)
    child2 = ''.join(child2)

    return child1, child2


def anular(p1, p2):
    gen1 = p1.get_gen
    gen2 = p2.get_gen

    index_nr = min(len(gen1), len(gen2))  # Calculate the maximum index for anular crossover

    n = random.randint(0, index_nr - 1)  # Randomly select the crossover point

    child1 = []
    child2 = []

    for i in range(index_nr):
        if i < n:
            child1[i] = gen1[i]
            child2[i] = gen2[i]
        else:
            child1[i] = gen2[i]
            child2[i] = gen1[i]

    child1 = ''.join(child1)
    child2 = ''.join(child2)

    return child1, child2

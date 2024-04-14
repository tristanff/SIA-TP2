import random
from src.character import *


def crossover(parent1, parent2, method, rate):
    # Check if crossover will occur
    if random.random() > rate:
        return parent1, parent2
        
    # If crossover occurs, apply the selected method
    try:
        child1_genes, child2_genes = globals()[method+"_crossover"](parent1.get_genes(), parent2.get_genes())
        if sum(child1_genes[1:]) != 150:
            child1_genes = repair(child1_genes)
        if sum(child2_genes[1:]) != 150:
            child2_genes = repair(child2_genes)
        return Character(parent1.name, *child1_genes), Character(parent1.name, *child2_genes)
    except:
        raise ValueError("Invalid crossover method: {}".format(method))


def repair(child):
    total_attributes = sum(child[1:])
    normalized_attributes = [round((attr / total_attributes) * 150, 3) for attr in child[1:]]
    return child[0], *normalized_attributes


def one_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def two_point_crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
    child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]
    return child1, child2


def uniform_crossover(parent1, parent2):
    child1 = []
    child2 = []
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < 0.5:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)
    return child1, child2


def annular_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[crossover_point:] + parent2[:crossover_point]
    child2 = parent2[crossover_point:] + parent1[:crossover_point]
    return child1, child2


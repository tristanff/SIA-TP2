import random
import numpy as np
import math


def selection(population, config):
    # Pick selection method based on selection probability
    if random.random() < float(config['selection']['selection_probability']):
        method = config['selection']['method1']
    else:
        method = config['selection']['method2']

    # Select parents based on the chosen selection method
    if method == 'elite':
        num_parents = int(config['selection']['selection_amount'])
        return elite_selection(population, num_parents)
    elif method == 'roulette':
        num_parents = int(config['selection']['selection_amount'])
        return roulette_wheel_selection(population, num_parents)
    elif method == 'universal':
        num_parents = int(config['selection']['selection_amount'])
        return universal_selection(population, num_parents)
    elif method == 'boltzmann':
        t0 = float(config['selection']['t0'])
        t1 = float(config['selection']['t1'])
        k = float(config['selection']['k'])
        num_parents = int(config['selection']['selection_amount'])
        temperature = t1 + (t0 - t1) * math.exp(-k * num_parents)
        return boltzmann_selection(population, num_parents, temperature)
    elif method == 'deterministic_tournament':
        num_parents = int(config['selection']['selection_amount'])
        tournament_size = int(config['selection']['tournament_size'])
        return deterministic_tournament_selection(population, num_parents, tournament_size)
    elif method == 'probabilistic_tournament':
        num_parents = int(config['selection']['selection_amount'])
        threshold = float(config['selection']['threshold'])
        return probabilistic_tournament_selection(population, num_parents, threshold)
    elif method == 'ranking':
        num_parents = int(config['selection']['selection_amount'])
        return ranking_selection(population, num_parents)
    else:
        raise ValueError("Invalid selection method: {}".format(config['selection']['method']))


def elite_selection(population, num_elites):
    # Sort the population based on performance in descending order
    sorted_population = sorted(population, key=lambda x: x.performance(), reverse=True)
    # Select the top individuals as elites
    elites = sorted_population[:num_elites]
    return elites


def roulette_wheel_selection(population, num_parents):
    # Calculate the sum of performances in the population
    fitness_sum = sum(individual.performance() for individual in population)
    # Calculate the probability for each individual
    probabilities = [individual.performance() / fitness_sum for individual in population]
    # Select parents using roulette wheel selection
    parents = np.random.choice(population, num_parents, p=probabilities)
    return parents


def universal_selection(population, num_parents):
    # Calculate the sum of performances
    fitness_sum = sum(individual.performance() for individual in population)

    # Check if the sum of performances is zero
    if fitness_sum == 0:
        raise ValueError("The sum of performances is zero.")

    # Calculate selection probabilities and cumulative probabilities
    probabilities = [individual.performance() / fitness_sum for individual in population]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]

    # Select parents
    selected_parents = []
    for _ in range(num_parents):
        # Generate a random pointer in the range [0, 1)
        pointer = random.random()

        # Find the individual corresponding to the pointer
        for i, cumulative_probability in enumerate(cumulative_probabilities):
            if pointer <= cumulative_probability:
                selected_parents.append(population[i])
                break

    return selected_parents


def boltzmann_selection(population, num_parents, temperature):
    # Calculate fitness values and exponential values
    fitness_values = [individual.performance() for individual in population]
    exp_values = [np.exp(fitness / temperature) for fitness in fitness_values]
    # Calculate probabilities
    probabilities = [exp_value / sum(exp_values) for exp_value in exp_values]
    # Select parent using Boltzmann selection
    parent = np.random.choice(population, num_parents, p=probabilities)
    return parent


def deterministic_tournament_selection(population, num_parents, tournament_size):
    selected_parents = []
    for _ in range(num_parents):
        # Select M individuals randomly
        tournament_candidates = random.sample(population, tournament_size)
        # Choose the best individual from the tournament
        best_individual = max(tournament_candidates, key=lambda individual: individual.performance())
        selected_parents.append(best_individual)
    return selected_parents


def probabilistic_tournament_selection(population, num_parents, threshold):
    selected_parents = []
    for _ in range(num_parents):
        # Select two individuals randomly
        ind1, ind2 = random.sample(population, 2)
        # Generate a random number in [0,1]
        r = random.uniform(0, 1)
        # Select the most fit or least fit individual based on the threshold
        if r < threshold:
            selected_individual = max(ind1, ind2, key=lambda individual: individual.performance())
        else:
            selected_individual = min(ind1, ind2, key=lambda individual: individual.performance())
        selected_parents.append(selected_individual)
    return selected_parents


def ranking_selection(population, num_parents):
    # Sort the population based on performance in descending order
    sorted_population = sorted(population, key=lambda x: x.performance(), reverse=True)
    # Calculate selection probabilities
    probabilities = [2 * (i + 1) / (len(population) * (len(population) + 1)) for i in range(len(population))]
    # Select parents using ranking selection
    parents = np.random.choice(sorted_population, num_parents, p=probabilities)
    return parents


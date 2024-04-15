import configparser
import random
import numpy as np
import time
import json
from src.character import *
from src.selection import selection
from src.crossover import crossover
from src.mutation import mutation
from src.replacement import *


def read_config(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    config = {section: dict(parser.items(section)) for section in parser.sections()}
    return config


def generate_start_population(population_class, population_size):   
    population = []

    for _ in range(int(population_size)):
        height = round(random.uniform(1.3, 2), 3)

        attributes = np.random.random(5)

        # Calculate the sum of attributes
        total_attributes = sum(attributes)

        # Normalize the attributes to have a sum of 150
        normalized_attributes = [round((attr / total_attributes) * 150, 3) for attr in attributes]

        # Create the character instance with the normalized and rounded attributes
        individual = Character(population_class, height, *normalized_attributes)
        population.append(individual)

    return population


def genetic_algorithm(filename):
    config = read_config(filename)
    population = generate_start_population(config['population']['class'], config['population']['size'])

    best_max_performance = 0

    # Iteration through the generations
    print("gen     |time (s)|avg_fit |max_fit |   hei   str   agi   pro   res   lif")
    print("========|========|========|========|================================================")

    for generation in range(int(config['algorithm']['generations'])):
        # Start timer
        start_time = time.time()

        # Initialize new population
        offspring = []

        # Selection of parents
        selected_parents = selection(population, config)

        # Iterate through the selected parents to perform crossover and mutation
        for i in range(0, len(selected_parents), 2):
            # Crossover
            child1, child2 = crossover(selected_parents[i], selected_parents[i+1], config['crossover']['method'], float(config['crossover']['rate']))

            # Mutation
            child1 = mutation(child1, config['mutation']['method'], float(config['mutation']['rate']))
            child2 = mutation(child2, config['mutation']['method'], float(config['mutation']['rate']))

            # Add to new population
            offspring.append(child1)
            offspring.append(child2)

        # Replacement
        new_population = replacement(population, offspring, config)
        
        # Record and print results
        population = new_population
        performances = [individual.performance() for individual in population]
        max_performance = max(performances)
        avg_performance = np.mean(performances)

        # Record data for analysis
        x1.append(avg_performance)
        x2.append(best_max_performance)
        genes = [individual.get_genes() for individual in population]
        x3.append(np.sum(np.std(genes, axis=0)))

        # Record notable results
        end_time = time.time()
        max_fitness = round(max_performance, 2)
        avg_fitness = round(avg_performance, 2)
        time_elapsed = round(end_time - start_time, 2)
        max_genes = population[np.argmax(performances)].get_genes()
        max_genes = np.round(np.array(max_genes), 2)

        print(f" {generation}  \t| {time_elapsed:.0e}\t | {avg_fitness:.2f}  | {max_fitness:.2f}  | {max_genes}")
        
        if max_performance > best_max_performance:
            best_max_performance = max_performance
            best_genes = max_genes
            best_generation = generation
    
    # Print final results
    print("=====================END=======================")
    print(f"Best performance: {best_max_performance:.2f}")
    print(f"First found at generation: {best_generation}")
    print(f"Genes: {best_genes}")
    print("===============================================")

    # Save to output file
    with open("analysis/output", "w") as fp:
        json.dump([x1, x2, x3], fp)
 

x1 = []
x2 = []
x3 = []


genetic_algorithm('config.ini')

"""
import matplotlib.pyplot as plt
plt.plot(x2, label='best fitness found so far')
plt.plot(x1, label='generation average fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title("Evolution of average and max fitness")
plt.legend()
plt.show()


plt.figure()
plt.plot(x3)
plt.xlabel('Generation')
plt.ylabel('Diversity among population')
plt.title("Evolution of diversity of genes")
plt.legend()
plt.show()
"""
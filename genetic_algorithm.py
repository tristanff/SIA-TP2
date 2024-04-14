import configparser
import random
import numpy as np
import time
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
    print("gen     |max_fit |avg_fit |time (s)|detail  ")
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

        end_time = time.time()
        max_fitness = round(max_performance, 2)
        avg_fitness = round(avg_performance, 2)
        time_elapsed = round(end_time - start_time, 2)
        genes = population[np.argmax(performances)].get_genes()
        genes = np.round(np.array(genes), 2)

        print(f" {generation}  \t| {max_fitness:.2f}  | {avg_fitness:.2f}  | {time_elapsed:.0e}| {genes}")
        
        if max_performance > best_max_performance:    
            best_max_performance = max_performance
            best_genes = genes
            best_generation = generation
            
    print("=====================END=======================")
    print(f"Best performance: {best_max_performance}")
    print(f"First found at generation: {best_generation}")
    print(f"Genes: {best_genes}")
    print("===============================================")

genetic_algorithm('config.ini')
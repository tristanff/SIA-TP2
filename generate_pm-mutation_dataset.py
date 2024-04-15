import configparser
import random
import numpy as np
import time
import json
import pandas as pd
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
        total_attributes = sum(attributes)
        normalized_attributes = [round((attr / total_attributes) * 150, 3) for attr in attributes]
        individual = Character(population_class, height, *normalized_attributes)
        population.append(individual)
    return population

def calculate_diversity(population):
    genes_matrix = np.array([individual.get_genes() for individual in population])
    diversity = np.mean(np.std(genes_matrix, axis=0))
    return diversity



def genetic_algorithm(config, p_m_values, selection_methods):
    for selection_method in selection_methods:
        data = pd.DataFrame()  # DataFrame pour stocker la performance moyenne et la diversité par génération

        for p_m in p_m_values:
            config['mutation']['rate'] = str(p_m)
            config['selection']['method'] = selection_method
            population = generate_start_population(config['population']['class'], config['population']['size'])
            performances_by_generation = []
            diversities_by_generation = []

            for generation in range(int(config['algorithm']['generations'])):
                start_time = time.time()
                offspring = []
                selected_parents = selection(population, config)
                for i in range(0, len(selected_parents), 2):
                    child1, child2 = crossover(selected_parents[i], selected_parents[i + 1],
                                               config['crossover']['method'], float(config['crossover']['rate']))
                    child1 = mutation(child1, config['mutation']['method'], float(config['mutation']['rate']))
                    child2 = mutation(child2, config['mutation']['method'], float(config['mutation']['rate']))
                    offspring.append(child1)
                    offspring.append(child2)
                new_population = replacement(population, offspring, config)
                population = new_population
                avg_performance = np.mean([individual.performance() for individual in population])
                performances_by_generation.append(avg_performance)
                diversity = calculate_diversity(population)
                diversities_by_generation.append(diversity)
                end_time = time.time()
                print(
                    f"Generation {generation}: Average Performance = {avg_performance:.2f}, Diversity = {diversity:.2f}, Time Elapsed = {end_time - start_time:.2f} seconds")

            data[f'Performance_p_m_{p_m}'] = performances_by_generation
            data[f'Diversity_p_m_{p_m}'] = diversities_by_generation

        # Exporter le DataFrame en CSV
        data.to_csv(f"analysis/data_{selection_method}.csv", index_label='Generation')

        print(f"Results for selection method '{selection_method}' saved to data_{selection_method}.csv")


if __name__ == "__main__":
    config = read_config('config.ini')
    p_m_values = [0.1, 0.25, 0.5, 0.75, 0.9]
    selection_methods = ['elite', 'roulette', 'universal', 'boltzmann', 'deterministic_tournament',
                         'probabilistic_tournament', 'ranking']
    genetic_algorithm(config, p_m_values, selection_methods)


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


config = read_config('config.ini')
characters = generate_start_population(config['population']['class'], config['population']['size'])

# Iteration through the generations
print("gen     |max_fit |avg_fit |time (s)|detail  ")
print("========|========|========|========|================================================")

for generation in range(int(config['algorithm']['generations'])):
    start_time = time.time()
    # Generate offspring for generation
    new_population = []
    for _ in range(round(int(config['population']['size']) / 2)):
        # Selection
        selected_parents = selection(characters, config)

        # Crossover
        offspring1, offspring2 = crossover(*selected_parents, config['crossover']['method'], float(config['crossover']['rate']))

        # Mutation
        offspring1 = mutation(offspring1, config['mutation']['method'], float(config['mutation']['rate']))
        offspring2 = mutation(offspring2, config['mutation']['method'], float(config['mutation']['rate']))

        # Add to new population
        new_population.append(offspring1)
        new_population.append(offspring2)
    
    population = new_population
    performances = [individual.performance() for individual in population]
    max_performance = max(performances)
    avg_performance = np.mean(performances)
     
    end_time = time.time()
    max_fitness = round(max_performance, 2)
    avg_fitness = round(avg_performance, 2)
    time_elapsed = round(end_time - start_time, 2)
    genes = population[np.argmax(performances)].get_genes()


    print(f" {generation}  \t| {format(max_fitness, '.2f')}  | {format(avg_fitness, '.2f')}  | {format(time_elapsed, '.2f')}   | {genes}")
    

"""


from genetic_algorithm import selection_op, crossover_op, mutation_op

# Load configuration parameters
with open('config.json') as f:
    config = json.load(f)

def generate_start_population(population_size):
    character_names = ["Warrior", "Archer", "Defender", "Infiltrator"]
    population = []

    for character_name in character_names:
        for _ in range(population_size):
            height = round(random.uniform(1.3, 2), 3)

            attributes = np.random.random(5)

            # Calculate the sum of attributes
            total_attributes = sum(attributes)

            # Normalize the attributes to have a sum of 150
            normalized_attributes = [round((attr / total_attributes) * 150,3) for attr in attributes]

            # Create the character instance with the normalized and rounded attributes
            individual = Character(character_name, height, *normalized_attributes)
            population.append(individual)

    return population



# Initialize population
population = [Character.random(config['character_type']) for _ in range(config['population_size'])]

# Run the genetic algorithm
for _ in range(config['num_generations']):
    # Evaluate fitness
    fitnesses = [individual.performance() for individual in population]

    # Select parents
    parents = selection_op(population, fitnesses, config['selection_type'], config['num_parents'])

    # Perform crossover
    offspring = crossover_op(parents, config['crossover_rate'])

    # Apply mutation
    population = mutation_op(offspring, config['mutation_rate'])

# Return the best individual
best_individual = max(population, key=lambda individual: individual.performance())
"""
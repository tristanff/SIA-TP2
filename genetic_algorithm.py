import configparser
import random
import numpy as np
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
selected_parents = selection(characters, config)
offspring = crossover(selected_parents, config['crossover']['method'], config['crossover']['rate'])






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
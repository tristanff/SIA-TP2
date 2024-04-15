from src.character import *
import random
import json
import numpy as np
from src.crossover import one_point_crossover, two_point_crossover, uniform_crossover, annular_crossover
from src.mutation import uniform_mutation, multigene_mutation, gene_mutation
from src.selection import roulette_wheel_selection, elite_selection, universal_selection, boltzmann_selection, \
    ranking_selection , deterministic_tournament_selection ,probabilistic_tournament_selection
from src.replacement import *

with open('config.json') as config_file:
    config = json.load(config_file)


def generate_start_population(population_size):
    character_names = ["warrior", "archer", "defender", "infiltrator"]
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
characters = generate_start_population(100)

#Debugging code to display the characters generated
""""
for idx, character in enumerate(characters):
    print(f"Character {idx+1} ({character.name}):")
    print(f"  - Strength Items: {character.strength_items}")
    print(f"  - Agility Items: {character.agility_items}")
    print(f"  - Proficiency Items: {character.proficiency_items}")
    print(f"  - Resistance Items: {character.resistance_items}")
    print(f"  - Life Items: {character.life_items}")
    print(f"  - Performance : {character.performance()}")
    print()
"""

best_character = max(characters, key=lambda x: x.performance())

print(f"Best_Character : ({best_character.name}):")
print(f"  - Strength Items: {best_character.strength_items}")
print(f"  - Agility Items: {best_character.agility_items}")
print(f"  - Proficiency Items: {best_character.proficiency_items}")
print(f"  - Resistance Items: {best_character.resistance_items}")
print(f"  - Life Items: {best_character.life_items}")
print(f"  - Performance : {best_character.performance()}")

parent1 = random.choice(characters)
parent2 = random.choice(characters)

genes1 = parent1.get_genes()
genes2 = parent2.get_genes()


child1_one_point_genes, child2_one_point_genes = one_point_crossover(genes1, genes2)

child1_two_point_genes, child2_two_point_genes = two_point_crossover(genes1, genes2)

child1_uniform_genes, child2_uniform_genes = uniform_crossover(genes1, genes2)

child1_annular_genes, child2_annular_genes = annular_crossover(genes1, genes2)


print("One point crossover:")
print("Parent 1 genes:", genes1)
print("Parent 2 genes:", genes2)
print("Child 1 genes:", child1_one_point_genes)
print("Child 2 genes:", child2_one_point_genes)

print("\nTwo point crossover:")
print("Parent 1 genes:", genes1)
print("Parent 2 genes:", genes2)
print("Child 1 genes:", child1_two_point_genes)
print("Child 2 genes:", child2_two_point_genes)

print("\nUniform crossover:")
print("Parent 1 genes:", genes1)
print("Parent 2 genes:", genes2)
print("Child 1 genes:", child1_uniform_genes)
print("Child 2 genes:", child2_uniform_genes)

print("\nAnnular crossover:")
print("Parent 1 genes:", genes1)
print("Parent 2 genes:", genes2)
print("Child 1 genes:", child1_annular_genes)
print("Child 2 genes:", child2_annular_genes)



# Random Value for testing
num_parents = 3
num_elites = 3
temperature = 1.0
tournament_size = 1
threshold = 0.5


character = Character("warrior", 1.75, 30, 40, 50, 20, 10)

# Affichage des attributs avant la mutation
print("\nBefore mutation :")
print("Height:", character.height)
print("Strength items:", character.strength_items)
print("Agility items:", character.agility_items)
print("Proficiency items:", character.proficiency_items)
print("Resistance items:", character.resistance_items)
print("Life items:", character.life_items)

gene_mutation(character, 0.5)

print("\nAfter Gen Mutation :")
print("Height:", character.height)
print("Strength items:", character.strength_items)
print("Agility items:", character.agility_items)
print("Proficiency items:", character.proficiency_items)
print("Resistance items:", character.resistance_items)
print("Life items:", character.life_items)

# Mutation multigène
multigene_mutation(character,1)
# Mutation rate is set to 1 to test that it's actually working
print("\nAfter Multi Mutation :")
print("Height:", character.height)
print("Strength items:", character.strength_items)
print("Agility items:", character.agility_items)
print("Proficiency items:", character.proficiency_items)
print("Resistance items:", character.resistance_items)
print("Life items:", character.life_items)

character = Character("warrior", 1.75, 30, 40, 50, 20, 10)
uniform_mutation([character],1)

mutated_characters = uniform_mutation([character], 1)

for mutated_character in mutated_characters:
    print("\nAfter Uniform Mutation :")
    print("Height:", mutated_character.height)
    print("Strength items:", mutated_character.strength_items)
    print("Agility items:", mutated_character.agility_items)
    print("Proficiency items:", mutated_character.proficiency_items)
    print("Resistance items:", mutated_character.resistance_items)
    print("Life items:", mutated_character.life_items)


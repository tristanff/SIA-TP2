from src.character import Character
import random


def generate_start_population(population_size):
    character_names = ["Warrior", "Archer", "Defender", "Infiltrator"]
    population = []

    for character_name in character_names:
        for _ in range(population_size):
            height = round(random.uniform(1.3, 2), 3)

            #Generation of 4 random uniform float
            attributes = [random.uniform(10, 50) for _ in range(4)]

            #Technique used to be sure that the sum is always equal to 150
            total_attributes = sum(attributes)
            normalized_attributes = [attr / total_attributes * 150 for attr in attributes]
            normalized_attributes = [round(attr, 2) for attr in normalized_attributes]

            life_items = 150 - sum(normalized_attributes)

            # Créer l'instance du personnage avec les attributs normalisés et arrondis
            individual = Character(character_name, height, *normalized_attributes, life_items)
            population.append(individual)

    return population
characters = generate_start_population(100)


for idx, character in enumerate(characters):
    print(f"Character {idx+1} ({character.name}):")
    print(f"  - Strength Items: {character.strength_items}")
    print(f"  - Agility Items: {character.agility_items}")
    print(f"  - Proficiency Items: {character.proficiency_items}")
    print(f"  - Resistance Items: {character.resistance_items}")
    print(f"  - Life Items: {character.life_items}")
    print(f"  - Performance : {character.performance()}")
    print()


best_character = max(characters, key=lambda x: x.performance())

print(f"Best_Character {idx + 1} ({best_character.name}):")
print(f"  - Strength Items: {best_character.strength_items}")
print(f"  - Agility Items: {best_character.agility_items}")
print(f"  - Proficiency Items: {best_character.proficiency_items}")
print(f"  - Resistance Items: {best_character.resistance_items}")
print(f"  - Life Items: {best_character.life_items}")
print(f"  - Performance : {best_character.performance()}")




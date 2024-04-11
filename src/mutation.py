import random


# Only one gene of one individual mutate
def gene_mutation(individual, mutation_rate):
    mutated_individual = individual
    if random.random() < mutation_rate:
        gene_to_mutate = random.choice(["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"])
        if gene_to_mutate == "height":
            mutated_individual.height = max(round(random.uniform(1.3, 2), 3), 1.3)  # Ensure height is not below 1.3
        else:
            current_value = getattr(individual, gene_to_mutate)
            mutated_value = round(current_value + random.uniform(-10, 10), 3)   # TO DO - Change this to make sure values are never below 0
            setattr(mutated_individual, gene_to_mutate, mutated_value)
    return mutated_individual

# Multiple genes of one invidual can mutate
def multigene_mutation(individual, mutation_rate):
    mutated_individual = individual
    for gene in ["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"]:
        if random.random() < mutation_rate:
            current_value = getattr(individual, gene)
            mutated_value = round(current_value + random.uniform(-10, 10), 3)  # TO DO - Change this to make sure values are never below 0
            setattr(mutated_individual, gene, mutated_value)
    return mutated_individual

# Multiple genes of multiples individuals can mutate
def uniform_mutation(individuals, mutation_rate):
    mutated_individuals = []
    for individual in individuals:
        mutated_individual = individual
        for gene in ["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"]:
            if random.random() < mutation_rate:
                current_value = getattr(individual, gene)
                mutated_value = round(current_value + random.uniform(-10, 10), 3)  # TO DO - Change this to make sure values are never below 0
                setattr(mutated_individual, gene, mutated_value)
        mutated_individuals.append(mutated_individual)
    return mutated_individuals
import random


def mutation(individual, method, rate):
    # Check if the individual will mutate
    if random.random() > rate:
        return individual

    # If the individual will mutate, apply the mutation algorithm
    try:
        return globals()[method+"_mutation"](individual, rate)
    except:
        raise ValueError("Invalid mutation method: {}".format(method))


# Only one gene of one individual mutate
def gene_mutation(individual, mutation_rate):
    mutated_individual = individual
    if random.random() < mutation_rate:
        gene_to_mutate = random.choice(
            ["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"])
        if gene_to_mutate == "height":
            mutated_individual.height = max(round(random.uniform(1.3, 2), 3), 0.0)  # Ensure height is between 1.3 and 2
        else:
            current_value = getattr(individual, gene_to_mutate)
            mutated_value = max(round(current_value + random.uniform(-10, 10), 3), 0)  # Ensure values are never below 0
            setattr(mutated_individual, gene_to_mutate, mutated_value)

            total_items = round(mutated_individual.strength_items + mutated_individual.agility_items +
                                mutated_individual.proficiency_items + mutated_individual.resistance_items +
                                mutated_individual.life_items, 2)
            if total_items != 150:
                factor = 150 / total_items
                mutated_individual.strength_items *= factor
                mutated_individual.agility_items *= factor
                mutated_individual.proficiency_items *= factor
                mutated_individual.resistance_items *= factor
                mutated_individual.life_items *= factor

    return mutated_individual


# Multiple genes of one invidual can mutate
def multigene_mutation(individual, mutation_rate):
    mutated_individual = individual
    for gene in ["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"]:
        if random.random() < mutation_rate:
            current_value = getattr(individual, gene)
            mutated_value = max(round(current_value + random.uniform(-10, 10), 3), 0)  # Make sure values are never below 0
            setattr(mutated_individual, gene, mutated_value)

        total_items = round(mutated_individual.strength_items + mutated_individual.agility_items +
                            mutated_individual.proficiency_items + mutated_individual.resistance_items +
                            mutated_individual.life_items, 2)
        if total_items != 150:
            factor = 150 / total_items
            mutated_individual.strength_items *= factor
            mutated_individual.agility_items *= factor
            mutated_individual.proficiency_items *= factor
            mutated_individual.resistance_items *= factor
            mutated_individual.life_items *= factor

        if random.random() < mutation_rate:
            mutated_individual.height = max(round(random.uniform(1.3, 2), 3), 0.0)  # Ensure height is between 1.3 and 2, and positive
    return mutated_individual


# Multiple genes of multiples individuals can mutate
def uniform_mutation(individuals, mutation_rate):
    mutated_individuals = []
    for individual in individuals:
        mutated_individual = individual
        for gene in ["height", "strength_items", "agility_items", "proficiency_items", "resistance_items", "life_items"]:
            if random.random() < mutation_rate:
                current_value = getattr(individual, gene)
                mutated_value = max(round(current_value + random.uniform(-10, 10), 3), 0)  # Make sure values are never below 0
                setattr(mutated_individual, gene, mutated_value)
            total_items = round(mutated_individual.strength_items + mutated_individual.agility_items +
                                mutated_individual.proficiency_items + mutated_individual.resistance_items +
                                mutated_individual.life_items, 2)
            if total_items != 150:
                factor = 150 / total_items
                mutated_individual.strength_items *= factor
                mutated_individual.agility_items *= factor
                mutated_individual.proficiency_items *= factor
                mutated_individual.resistance_items *= factor
                mutated_individual.life_items *= factor

            if random.random() < mutation_rate:
                mutated_individual.height = max(round(random.uniform(1.3, 2), 3),
                                                0.0)  # Ensure height is between 1.3 and 2, and positive
                
    return mutated_individuals


import random


def replacement(parent, child, replacement):
    if replacement == 'traditional':
        return traditional_replacement(parent, child)
    if replacement == 'youth':
        return youth_replacement(parent, child)


#metodo3
def traditional_replacement(parent, child):
    new_population = parent + child
    return random.sample(new_population, len(parent))


#metodo4
def youth_replacement(parent, child):
    if len(child) > len(parent):
        return random.sample(child, len(parent))
    return child + random.sample(parent, len(parent) - len(child))
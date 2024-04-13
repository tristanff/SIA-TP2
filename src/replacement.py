import random


def replacement_op(parent, child, replacement):
    if replacement == 'traditional':
        return traditional(parent, child)
    if replacement == 'youth':
        return youth(parent, child)

#metodo3
def traditional(parent, child):
    new_population = parent + child
    return random.sample(new_population, len(parent))


#metodo4
def youth(parent, child):
    if len(child) > len(parent):
        return random.sample(child, len(parent))
    return child + random.sample(parent, len(parent) - len(child))
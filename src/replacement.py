import random


def replacement(parent, child, config):
    # Pick replacement method based on replacement probability
    if random.random() < float(config['replacement']['replacement_probability']):
        method = config['replacement']['method1']
    else:
        method = config['replacement']['method2']
    
    # Select replacement method
    if method == 'traditional':
        return traditional_replacement(parent, child)
    elif method == 'youth':
        return youth_replacement(parent, child)
    else:
        raise ValueError("Invalid replacement method: {}".format(method))


#metodo3
def traditional_replacement(parent, child):
    new_population = parent + child
    return random.sample(new_population, len(parent))


#metodo4
def youth_replacement(parent, child):
    if len(child) > len(parent):
        return random.sample(child, len(parent))
    return child + random.sample(parent, len(parent) - len(child))
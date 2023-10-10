def warn_the_sheep(queue):
    for location in range(len(queue)):
        if queue[-1 - location] == 'wolf':
            N = location
    return 'Pls go away and stop eating my sheep' if N == 0 else f'Oi! Sheep number {N}! You are about to be eaten by a wolf!'

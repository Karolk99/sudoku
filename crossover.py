  
import numpy as np
import random
from math import sqrt

class Crossover:

    @staticmethod
    def crossover(parent1, parent2, size):
        parents = [parent1, parent2]
        children = [np.zeros((size, size), dtype=int), np.zeros((size, size), dtype=int)]
        block_size = int(sqrt(size))
        
        for i in range(size):
            for child in children:
                parent = random.choice(parents)
                x = int(i / block_size) * block_size
                y = i % block_size * block_size
                child[x:x+block_size, y:y+block_size] = parent[x:x+block_size, y:y+block_size]
        return children



        
        

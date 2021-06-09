  
import numpy as np
import random
from math import sqrt

class Crossover:


    @staticmethod
    def crossover(parent1, parent2, size, method):
        if method == 0:
            return Crossover.crossover_method1(parent1, parent2, size)
        else:
            return Crossover.crossover_method2(parent1, parent2, size)

    @staticmethod
    def crossover_method1(parent1, parent2, size):
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

    @staticmethod
    def crossover_method2(parent1, parent2, size):
        parents = [parent1, parent2]
        children = [np.zeros((size, size), dtype=int), np.zeros((size, size), dtype=int)]
        
        for i in range(size):
            for child in children:
                parent = random.choice(parents)
                child[i] = parent[i]
        return children



        
        

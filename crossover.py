import numpy as np
import random
from math import sqrt

class Crossover:

    @staticmethod
    def crossover(parent1, parent2, size):
        parents = [parent1, parent2]
        children = [np.zeros((9, 9), np.zeros(9, 9))]
        block_size = sqrt(size)
        
        for i in range(size):
            for child in children:
                parent = random.choice(parents)
                x = i / block_size
                y = (i*block_size)%size
                child[x:x+block_size, y:y+block_size] = parent[x:x+block_size, y:y+block_size]
        return children
        


       




        
        

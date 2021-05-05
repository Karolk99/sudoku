from candidate import Candidate
from random import randint

class Population():
    
    def __init__(self, size : int=9):
        self.candidates = None
        self.size = size

    def create_population(self, candidates_no):
        self.candidates = []

        for _ in range(0, candidates_no):
            candidate = Candidate()
            candidate.fill_in_array() # dopracować
            self.candidates.append(candidate)
        
        self.udpate_fitness()
    
    def udpate_fitness(self):
        for candidate in self.candidates:
            candidate.udpate_fitness()
    
    def sort(self):
        self.candidates.sort(self.sort_fitness)

    def sort_fitness(self, x, y):
        if(x.fitness < y.fitness):
            return 1
        elif(x.fitness == y.fitness):
            return 0
        else:
            return -1
        
    def compete(self):
        c1 = self.candidates[randint(0, len(self.candidates) - 1)]
        c2 = self.candidates[randint(0, len(self.candidates) - 1)]

        if(c1.fitness >= c2.fitness):
            return c1
        else: 
            return c2
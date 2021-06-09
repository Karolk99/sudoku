from candidate import Candidate
from candidate2 import Candidate2
from random import randint

class Population():
    
    def __init__(self, size : int=9):
        self.candidates = None
        self.size = size

    def create_population(self, candidates_no, method):
        self.candidates = []

        for _ in range(0, candidates_no):
            candidate = Candidate(method)
            if method == 0:
                candidate = Candidate()
            else:
                candidate = Candidate2()
            candidate.fill_in_array()
            self.candidates.append(candidate)
        
        self.udpate_fitness()
        self.sort()
    
    def udpate_fitness(self):
        for candidate in self.candidates:
            candidate.udpate_fitness()
    
    def sort(self):
        #self.candidates.sort(key=self.sort_fitness)
        self.candidates.sort(key=lambda x: x.fitness, reverse=True)
    
    @staticmethod
    def sort_fitness(x, y):
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
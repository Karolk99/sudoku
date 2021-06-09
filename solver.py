from candidate import Candidate
from population import Population
from crossover import Crossover
import numpy as np

class Solver():

    def __init__(self):
        pass
    
    def solve(self, candidates_no, elites_no, generation_no, method):
        self.population = Population(9)
        self.population.create_population(candidates_no, method)
        
        fitness_history = []

        for generation in range(generation_no):
            
            print("Generation %d" % generation)
            
            self.population.sort()
            best_fitness = self.population.candidates[0].fitness
            
            fitness_history.append(best_fitness)

            if best_fitness >= 1.0:
                print("solution founded")
                return self.population.candidates[0], fitness_history
            
            print("Best fitness: %f" % best_fitness)

            next_population = []

            elites = []
            for i in range(elites_no):
                elite = Candidate()
                elite.array = np.copy(self.population.candidates[i].array)
                elites.append(elite)
            
            for _ in range(elites_no, candidates_no, 2):
                parent1 = self.population.compete()
                parent2 = self.population.compete()

                child1 = Candidate(9)
                child2 = Candidate(9)

                arrays = Crossover.crossover(parent1.array, parent2.array, 9, method)
                child1.array, child2.array = arrays[0], arrays[1]

                child1.mutate()
                child2.mutate()

                child1.udpate_fitness()
                child2.udpate_fitness()

                child1.mutate()
                child2.mutate()

                next_population.append(child1)
                next_population.append(child2)
            
            for e in elites:
                next_population.append(e)
            
            self.population.candidates = next_population
            self.population.udpate_fitness()
        return None, fitness_history

    @staticmethod
    def read_puzzle_from_file(path : str) -> list:
        Candidate.static_fields = np.zeros((9, 9), dtype=int)
        fields = open(path).readlines()
        
        for i in range(len(fields)):
            fields[i] = fields[i].split(',')
            fields[i][2] = fields[i][2][:-1]
            fields[i] = tuple(fields[i])

            Candidate.static_fields[int(fields[i][0])][int(fields[i][1])] = int(fields[i][2])
        
    





if __name__ == '__main__':

    Solver.read_puzzle_from_file(path="sudoku/puzzles/puzzle2.txt")
    # Candidate.static_fields = np.zeros((9, 9), dtype=int)
    # solution = Solver().solve(elites_no=50, candidates_no=1000, generation_no=10000)
    # print(solution.array)
    # print(Candidate.static_fields)
    # candidate = Candidate(9)
    # candidate.fill_in_array()
    # print(candidate.array)
    # candidate.mutate()
    # print(candidate.array)
    # candidate.udpate_fitness()
    # print(candidate.fitness)
    # population = Population(9)
    # population.create_population(100)
    # s = population.compete()
    # print(s.fitness)
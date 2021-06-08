import solver
import numpy as np
from candidate import Candidate
import matplotlib.pyplot as plt

def test(candidates_no, elites_no, generation_no, plot: bool, file: str) -> None:
    
    if file == '':
        Candidate.static_fields = np.zeros((9, 9), dtype=int)
    else:
        solver.Solver.read_puzzle_from_file(file)
    
    solution, fitness_history = solver.Solver().solve(candidates_no, elites_no, generation_no)

    generations = [ i for i in range(len(fitness_history))]

    if plot:
        plt.plot(generations, fitness_history)
    
        plt.xlabel('Generacja')

        plt.ylabel('Fitness')
        
        plt.title('Algorytm genetyczny')
        
        plt.show()


if __name__ == '__main__':
    test(1000, 50, 1000, True, '')
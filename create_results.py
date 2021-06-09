import solver
import numpy as np
from candidate import Candidate
import matplotlib.pyplot as plt

path = 'results/plot'
extension = '.png'

def test(candidates_no, elites_no, generation_no, method, plot: bool, file: str) -> None:
    
    if file == '':
        Candidate.static_fields = np.zeros((9, 9), dtype=int)
    else:
        solver.Solver.read_puzzle_from_file(file)
    
    solution, fitness_history = solver.Solver().solve(candidates_no, elites_no, generation_no, method)

    generations = [ i for i in range(len(fitness_history))]

    if plot:
        plt.plot(generations, fitness_history)
    
        plt.xlabel('Generacja')

        plt.ylabel('Fitness')
        
        plt.title(f'Algorytm genetyczny')
        
        txt = f'parametry: elita: {elites_no}, populacja: {candidates_no}, liczba generacji: {generation_no}. Wersja: {"wierszowa" if method else "blokowa"}'
        plt.text(5, -.13, txt, ha='center')
        fig = plt.gcf()
        fig.set_size_inches(10, 6)
        plt.axis([0, generation_no, 0, 1])

        filename = (path + '_' + str(candidates_no) + '_' + str(elites_no) + 
                             '_' + str(generation_no) + '_' + str(method) + extension)
        plt.savefig(filename)

def make_tests(files, arguments_list):
    for path in files:
        for arguments in arguments_list:
            candidates_no, elites_no, generation_no, method = arguments
            test(candidates_no, elites_no, generation_no, method, True, path)
        
if __name__ == '__main__':
    path = 'puzzles/'
    files = ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']
    
    test(1000, 50, 500, 1, True, 'puzzles/puzzle1.txt')
    test(1000, 50, 500, 0, True, 'puzzles/puzzle1.txt')

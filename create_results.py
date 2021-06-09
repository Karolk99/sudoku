import solver
import numpy as np
from candidate import Candidate
import matplotlib.pyplot as plt

plot_path = 'results/plot'
extension = '.png'

def test(candidates_no, elites_no, generation_no, method, file: str):
    if file == '':
        Candidate.static_fields = np.zeros((9, 9), dtype=int)
    else:
        solver.Solver.read_puzzle_from_file(file)
    solution, fitness_history = solver.Solver().solve(candidates_no, elites_no, generation_no, method)
    return fitness_history

def make_tests(files, arguments_list):
    dir = 'puzzles/'
    for path in files:
        for arguments in arguments_list:
            print(arguments)
            candidates_no, elites_no, generation_no = arguments
            fitness_history = []
            for method in (0, 1):
                fitness_history.append(test(candidates_no, elites_no, generation_no, method, dir + path))
            generations0 = [ i for i in range(len(fitness_history[0]))]
            generations1 = [ i for i in range(len(fitness_history[1]))]
            plt.plot(generations0, fitness_history[0], label=f'{"wierszowa"}')
            plt.plot(generations1, fitness_history[1], label=f'{"blokowa"}')
            plt.legend()
            plt.xlabel('Generacja')
            plt.ylabel('Fitness')
            plt.title('Algorytm genetyczny')
            txt = f'parametry: elita: {elites_no}, populacja: {candidates_no}, liczba generacji: {generation_no}.'
            plt.text(generation_no/2, -.13, txt, ha='center')
            fig = plt.gcf()
            fig.set_size_inches(10, 6)
            plt.axis([0, generation_no, 0, 1])

            filename = (plot_path + '_' + str(candidates_no) + '_' + str(elites_no) + 
                                '_' + str(generation_no) + '_' + extension)
            plt.savefig(filename)
            plt.cla()
        
if __name__ == '__main__':
    files = ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']
    arguments_list = [
        (200, 50, 1000),
        (400, 20, 1000),
    ]
    make_tests(['puzzle1.txt'], [(200, 50, 10)])
    
    #test(1000, 50, 500, 1, True, 'puzzles/puzzle1.txt')
    #test(1000, 50, 500, 0, True, 'puzzles/puzzle1.txt')

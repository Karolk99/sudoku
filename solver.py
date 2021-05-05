from candidate import Candidate
import numpy as np

class Solver():

    def __init__(self, path: str):
        pass

    @staticmethod
    def read_puzzle_from_file(path : str) -> list:
        Candidate.static_fields = np.zeros((9, 9))
        fields = open(path).readlines()
        
        for i in range(len(fields)):
            fields[i] = fields[i].split(',')
            fields[i][2] = fields[i][2][:-1]
            fields[i] = tuple(fields[i])

            Candidate.static_fields[int(fields[i][0])][int(fields[i][1])] = int(fields[i][2])
        

if __name__ == '__main__':

    Solver.read_puzzle_from_file(path="sudoku/puzzles/puzzle1.txt")
    print(Candidate.static_fields)
    candidate = Candidate(9)
    candidate.fill_in_array()
    print(candidate.array)

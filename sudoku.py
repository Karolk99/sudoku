import numpy as np
import random 

class Sudoku:
    def __init__(self, size=9):
        self.size=9
        self.array=np.zeros((size, size))
    
    def create_sudoku_puzzle(self):
        
        numbers = [x for x in range(1, self.size + 1) for i in range(1, self.size + 1)]
        
        for row in self.array:
            for i in range(len(row)):
                value = numbers[random.randint(0, len(numbers) - 1)]
                numbers.remove(value)
                row[i] = value
                
    def __shufle(self):
        pass                                #do ustalenia




if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.create_sudoku_puzzle()
    print(sudoku.array)
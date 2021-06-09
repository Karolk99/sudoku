import numpy as np
import random
import sys


class Candidate2:
    static_fields = []

    def __init__(self, size=9):
        self.size = 9
        self.array = np.zeros((size,size), dtype=int)
        self.fitness = None

    def udpate_fitness(self):
        row_count = np.zeros(self.size)
        column_count = np.zeros(self.size)
        block_count = np.zeros(self.size)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        for i in range(0, self.size):
            block_x = (i % 3) * 3
            block_y = (i // 3) * 3
            for x in range(3):
                for y in range(3):
                    block_count[int(self.array[block_x + x][block_y + y])-1] += 1

            block_sum += (1.0/len(set(block_count)))/self.size
            block_count = np.zeros(self.size)

        for i in range(0, self.size):
            for j in range(0, self.size):
                column_count[int(self.array[j][i]-1)] += 1

            column_sum += (1.0 / len(set(column_count)))/self.size
            column_count = np.zeros(self.size)

        if (int(block_sum) == 1 and int(column_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum
        
        self.fitness = fitness
    

    def mutate(self):

        row = random.randint(0, self.size-1)
        col1 = random.randint(0, self.size-1)
        col2 = random.randint(0, self.size-1)
        
        while col1 == col2 or Candidate2.static_fields[row][col1] != 0 or Candidate2.static_fields[row][col2] != 0:
            col1 = random.randint(0, self.size - 1)
            col2 = random.randint(0, self.size - 1)
        self.array[row][col1], self.array[row][col2] = self.array[row][col2], self.array[row][col1]
    
    def create_sudoku_puzzle(self) -> None:
        if self.array is None:
            self.array = np.zeros((self.size, self.size))

        numbers = [x for x in range(1, self.size + 1) for _ in range(1, self.size + 1)]
        
        for row in self.array:
            for i in range(len(row)):
                value = numbers[random.randint(0, len(numbers) - 1)]
                numbers.remove(value)
                row[i] = value
                
    def choose_static_fields_manually(self) -> None:
        self.array = np.zeros((self.size, self.size))
        Candidate2.static_fields = np.zeros((9, 9))

        print("To end type end. Correct field example: 2,3. Correct value example: 2")

        while True:
            field = input("choose static field:")
            if field == "end":
                break
            field = field.split(',')
            value = int(input("choose value for this field:"))
            
            try:
                self.array[field[0]][field[1]] = value
                Candidate2.static_fields[field[0]][field[1]] = value
            except:
                print("Oops!", sys.exc_info()[0], "occurred. Try again")

    def choose_static_fields(self, fields : list=None, path : str=None) -> None:
        self.array = np.zeros((self.size, self.size))
        Candidate2.static_fields = np.zeros((9, 9))

        if path != None:
            fields = self.read_puzzle_from_file(path)

        for count, field in enumerate(fields):  # field is a tuple looking like this: (x, y, value)
            try:
                self.array[field[0]][field[1]] = field[2]
                Candidate2.static_fields[field[0]][field[1]] = field[2]
            except:
                print("Oops!", sys.exc_info()[0], "occurred.", end=' ')
                print(f"In {count} element")

    def fill_in_array(self) -> None:
        if self.array is None:
            self.array = np.copy(Candidate2.static_fields) #np.zeros((self.size, self.size))
            
        for i in range(9):
            numbers = [ x for x in range(1, 10)]
            
            for j in range(9):
                if self.array[i][j] != 0:
                    numbers.remove(self.array[i][j])

            for j in range(9):
                if self.array[i][j] == 0:
                    value = numbers[random.randint(0, len(numbers) - 1)]
                    numbers.remove(value)
                    self.array[i][j] = value
         
    @staticmethod
    def read_puzzle_from_file(path : str) -> list:
        fields = open(path).readlines()
        
        for i in range(len(fields)):
            fields[i] = fields[i].split(',')
            fields[i][2] = fields[i][2][:-1]
            fields[i] = tuple(fields[i])
        
        return fields
                

if __name__ == '__main__':
    sudoku = Candidate2()
    Candidate2.static_fields = np.zeros((9, 9), dtype=int)
    fields = open('puzzles/puzzle1.txt').readlines()
    
    for i in range(len(fields)):
        print(fields[i])
        fields[i] = fields[i].split(',')
        fields[i][2] = fields[i][2][:-1]
        fields[i] = tuple(fields[i])

        Candidate2.static_fields[int(fields[i][0])][int(fields[i][1])] = int(fields[i][2])
    print(sudoku.array)
    sudoku.fill_in_array()
    print(sudoku.array)
    sudoku.udpate_fitness()
    print(sudoku.fitness)
    for i in range(100000):
        sudoku.mutate()
        sudoku.udpate_fitness()
    print(sudoku.fitness)
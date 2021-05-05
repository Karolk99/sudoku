import numpy as np
import random
import sys


class Candidate:
    static_fields = []

    def __init__(self, size=9):
        self.size = 9
        self.array = None 
        self.fitness = None

    def udpate_fitness(self):
        row_count = np.zeros(self.size)
        column_count = np.zeros(self.size)
        block_count = np.zeros(self.size)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        for i in range(0, self.size):
            for j in range(0, self.size):
                row_count[self.array[i][j]-1] += 1

            row_sum += (1.0/len(set(row_count)))/self.size
            row_count = np.zeros(self.size)

        for i in range(0, self.size):
            for j in range(0, self.size):
                column_count[self.array[j][i]-1] += 1

            column_sum += (1.0 / len(set(column_count)))/self.size
            column_count = np.zeros(self.size)

        for i in range(0, self.size, 3):
            for j in range(0, self.size, 3):
                block_count[self.array[i][j]-1] += 1
                block_count[self.array[i][j+1]-1] += 1
                block_count[self.array[i][j+2]-1] += 1
                
                block_count[self.array[i+1][j]-1] += 1
                block_count[self.array[i+1][j+1]-1] += 1
                block_count[self.array[i+1][j+2]-1] += 1
                
                block_count[self.array[i+2][j]-1] += 1
                block_count[self.array[i+2][j+1]-1] += 1
                block_count[self.array[i+2][j+2]-1] += 1

                block_sum += (1.0/len(set(block_count)))/self.size
                block_count = np.zeros(self.size)

        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum
        
        self.fitness = fitness
    

    def mutate(self): # in 3x3 block

        block_no = random.randint(0, self.size - 1)
        x_swap = random.randint(0, self.size - 1)
        y_swap = random.randint(0, self.size - 1)
        
        while x_swap == y_swap:
            x_swap = random.randint(0, self.size - 1)
            y_swap = random.randint(0, self.size - 1)
        
        x, y = block_no % 3, block_no // 3
        
        self.array[x + (x_swap % 3)][y + (x_swap // 3)], self.array[x + (y_swap % 3)][y + (y_swap // 3)] = self.array[x + (y_swap % 3)][y + (y_swap // 3)], self.array[x + (x_swap % 3)][y + (x_swap // 3)]

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
        Candidate.static_fields = np.zeros((9, 9))

        print("To end type end. Correct field example: 2,3. Correct value example: 2")

        while True:
            field = input("choose static field:")
            if field == "end":
                break
            field = field.split(',')
            value = int(input("choose value for this field:"))
            
            try:
                self.array[field[0]][field[1]] = value
                Candidate.static_fields[field[0]][field[1]] = value
            except:
                print("Oops!", sys.exc_info()[0], "occurred. Try again")

    def choose_static_fields(self, fields : list=None, path : str=None) -> None:
        self.array = np.zeros((self.size, self.size))
        Candidate.static_fields = np.zeros((9, 9))

        if path != None:
            fields = self.read_puzzle_from_file(path)

        for count, field in enumerate(fields):  # field is a tuple looking like this: (x, y, value)
            try:
                self.array[field[0]][field[1]] = field[2]
                Candidate.static_fields[field[0]][field[1]] = field[2]
            except:
                print("Oops!", sys.exc_info()[0], "occurred.", end=' ')
                print(f"In {count} element")

    def fill_in_array(self) -> None:
        if self.array is None:
            self.array = np.zeros((self.size, self.size))

        #numbers = [x for x in range(1, self.size + 1) for _ in range(1, self.size + 1)]

        #for value in Candidate.static_fields:
        #    numbers.remove(value)
        
        # for row_no, row in enumerate(self.array):
        #     for i in range(len(row)):
        #         if (row_no, i) not in Candidate.static_fields:
        #             value = numbers[random.randint(0, len(numbers) - 1)]
        #             numbers.remove(value)
        #             row[i] = value
        for i in range(self.size):
            
    @staticmethod
    def read_puzzle_from_file(path : str) -> list:
        fields = open(path).readlines()
        
        for i in range(len(fields)):
            fields[i] = fields[i].split(',')
            fields[i][2] = fields[i][2][:-1]
            fields[i] = tuple(fields[i])
        
        return fields
            
    def __shufle(self):
        pass                                #do ustalenia, np mozemy narazie zalozyc, ze wszystkie pola sa ruchome to wtedy wydaje sie to byc prosty
                                       #do rozwiazania problem np tasujemy tak zeby zawsze dojsc do tego samego ulozenia (mamy jakis wzorzec ) ale to tylko sugestia :)

if __name__ == '__main__':
    sudoku = Candidate()
    sudoku.read_puzzle_from_file("sudoku/puzzles/puzzle1.txt")
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
    

    def mutate(self):

        block_no = random.randint(0, self.size - 1)
        x_swap = random.randint(0, self.size - 1)
        y_swap = random.randint(0, self.size - 1)
        
        block_x, block_y = block_no % 3, block_no // 3
        x1, y1 = block_x * 3 + (x_swap % 3), block_y * 3 + (x_swap // 3)
        x2, y2 = block_x * 3 + (y_swap % 3), block_y * 3 + (y_swap // 3)

        while x_swap == y_swap or Candidate.static_fields[x1][y1] != 0 or Candidate.static_fields[x2][y2] != 0:
            x_swap = random.randint(0, self.size - 1)
            y_swap = random.randint(0, self.size - 1)
            x1, y1 = block_x * 3 + (x_swap % 3), block_y * 3 + (x_swap // 3)
            x2, y2 = block_x * 3 + (y_swap % 3), block_y * 3 + (y_swap // 3)
        
        self.array[x1][y1], self.array[x2][y2] = self.array[x2][y2], self.array[x1][y1]

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
            self.array = np.copy(Candidate.static_fields) #np.zeros((self.size, self.size))
        
        for i in range(9):
            block_x = (i % 3) * 3
            block_y = (i // 3) * 3
            
            numbers = [ x for x in range(1, 10)]
            
            for x in range(3):
                for y in range(3):
                    if self.array[block_x + x][block_y + y] != 0:
                        print(self.array[block_x + x][block_y + y])
                        numbers.remove(self.array[block_x + x][block_y + y])
            print()
            for x in range(3):
                for y in range(3): 
                    if self.array[block_x + x][block_y + y] == 0:
                        value = numbers[random.randint(0, len(numbers) - 1)]
                        numbers.remove(value)
                        self.array[block_x + x][block_y + y] = value
         
    @staticmethod
    def read_puzzle_from_file(path : str) -> list:
        fields = open(path).readlines()
        
        for i in range(len(fields)):
            fields[i] = fields[i].split(',')
            fields[i][2] = fields[i][2][:-1]
            fields[i] = tuple(fields[i])
        
        return fields
                

if __name__ == '__main__':
    sudoku = Candidate()
    sudoku.read_puzzle_from_file("sudoku/puzzles/puzzle1.txt")
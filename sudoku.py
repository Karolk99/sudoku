import numpy as np
import random 
import sys


class Sudoku:
    def __init__(self, size=9):
        self.size = 9
        self.array = None 
        self.static_fields = None

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
        self.static_fields = {}

        print("To end type end. Correct field example: 2,3. Correct value example: 2")

        while True:
            field = input("choose static field:")
            if field == "end":
                break
            field = field.split(',')
            value = int(input("choose value for this field:"))
            
            try:
                self.array[field[0]][field[1]] = value
                self.static_fields[tuple(field)] = value
            except:
                print("Oops!", sys.exc_info()[0], "occurred. Try again")

    def choose_static_fields(self, fields : list) -> None:
        self.array = np.zeros((self.size, self.size))
        self.static_fields = {}

        for count, field in enumerate(fields):  # field is a tuple looking like this: (x, y, value)
            try:
                self.array[field[0]][field[1]] = field[2]
                self.static_fields[tuple(field[:2])] = field[2]
            except:
                print("Oops!", sys.exc_info()[0], "occurred.", end=' ')
                print(f"In {count} element")

    def fill_in_array(self) -> None:
         if self.array is None:
            self.array = np.zeros((self.size, self.size))

        numbers = [x for x in range(1, self.size + 1) for _ in range(1, self.size + 1)]

        for _, value in self.static_fields.items():
            numbers.remove(value)
        
        for row_no, row in enumerate(self.array):
            for i in range(len(row)):
                if (row_no, i) not in self.static_fields:
                    value = numbers[random.randint(0, len(numbers) - 1)]
                    numbers.remove(value)
                    row[i] = value

    def __shufle(self):
        pass                                #do ustalenia, np mozemy narazie zalozyc, ze wszystkie pola sa ruchome to wtedy wydaje sie to byc prosty
                                       #do rozwiazania problem np tasujemy tak zeby zawsze dojsc do tego samego ulozenia (mamy jakis wzorzec ) ale to tylko sugestia :)




if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.create_sudoku_puzzle()
    print(sudoku.array)
from printBoard import *

solutions = []

class SolveBoard():
    def __init__(self, board, base, print):
        self.board = board
        self.base = base
        self.size = self.base*self.base
        self.print = print
        self.solved = False
        self.solutions = [] 
        
    def check(self, row, column, number):
        #Check for Rows
        for i in range(0,self.size):
            if self.board[row][i] == number:
                return False

        #Check for columns
        for i in range(0,self.size):
            if self.board[i][column] == number:
                return False
        
        #Check for basexbase square
        x = (column // self.base) * self.base
        y = (row // self.base) * self.base
        for i in range(0,self.base):
            for j in range(0,self.base):
                if self.board[y+i][x+j] == number:
                    return False
        return True
    
    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self.board[row][column] == 0:
                    for number in range(1,10):
                        if self.check(row, column, number):
                            self.board[row][column] = number
                            self.solve()
                            self.board[row][column] = 0

                    return
        self.solved = True
        if self.print:
            self.toPrint()
        if self.solved:
            global solutions
            solutions.append(self.board)
            #print(solutions)
          
    def toPrint(self):
        if self.solved:
            PrintBoard(self.board).imprimir()
        else:
            print("The board could't be solved")
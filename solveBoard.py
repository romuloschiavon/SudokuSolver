from printBoard import *

grid = Board().board

class BoardSolver():
    def __init__(self, board, base):
        self.board = board
        self.base = base
        self.size = self.base*self.base
        self.solved = False
        
    def check(self, row, column, number):
        global grid
        
        #Check for Rows
        for i in range(0,self.size):
            if grid[row][i] == number:
                return False

        #Check for columns
        for i in range(0,self.size):
            if grid[i][column] == number:
                return False
        
        #Check for basexbase square
        x = (column // self.base) * self.base
        y = (row // self.base) * self.base
        for i in range(0,self.base):
            for j in range(0,self.base):
                if grid[y+i][x+j] == number:
                    return False
        return True
    
    def solve(self):
        global grid
        for row in range(0,9):
            for column in range(0,9):
                if grid[row][column] == 0:
                    for number in range(1,10):
                        if self.check(row, column, number):
                            grid[row][column] = number
                            self.solve()
                            grid[row][column] = 0

                    return
        self.solved = True        
        self.toPrint()
            
    def toPrint(self):
        if self.solved:
            PrintBoard(self.board).imprimir()
        else:
            print("The board could't be solved")
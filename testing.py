#Works
from solveBoard import *

grid = Board(base=3, print=False, square=25).board
PrintBoard(grid).imprimir()            
BoardSolver(grid, base=3, print=True).solve()
from board import *

class PrintBoard():
    def __init__(self, board):
        self.board = board
        
    def imprimir(self):
        Linha = " #########################"
        i = 0
        j = 0
        print("\n" + Linha, end="\n")
        global all_the_solutions
        for line in self.board:
            print(" ", end="")
            print("# ", end="")
            for value in line:
                i += 1
                if i == 4 or i == 7:
                    print("# ", end="")
                print(value, end=" ")
            print("#", end="\n")
            if j == 2 or j == 5:
                print(Linha)
            i = 0
            j += 1
        print(Linha, end="\n")
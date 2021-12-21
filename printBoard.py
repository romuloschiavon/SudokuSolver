from board import *

class printBoard():
    def __init__(self, base):
        self.base = base
        self.board = Board(base=self.base, print=False).board
        
    def imprimir(self):
        Linha = " #########################"
        i = 0
        j = 0
        print("\n" + Linha, end="\n")
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
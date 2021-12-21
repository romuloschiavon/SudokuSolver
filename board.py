import numpy as np
from random import sample

class Board():
    def __init__(self, base):
        self.base = base
        self.size = base*base
        self.board = self.createSolutionBoard()

    def pattern(self, r, c): 
        return (self.base*(r%self.base)+r//self.base+c)%self.size

    def createSolutionBoard(self):
        rangeBase = range(self.base)
        rows = [g*self.base + r for g in shuffle(rangeBase) for r in shuffle(rangeBase)]
        columns = [g*self.base + c for g in shuffle(rangeBase) for c in shuffle(rangeBase)]
        nums = shuffle(range(1, self.size+1))

        self.board = [[nums[self.pattern(r=r,c=c)] for c in columns] for r in rows]
        self.printSolutionBoard()
        return self.board

    def printSolutionBoard(self):
        print("\n")
        for line in self.board:
            print(line)
        print("\n")

    def createPuzzleBoard(self):
        square = self.size * self.size
        zeros = square * 3//4
        for p in sample(range(square), zeros):
            self.board[p//self.size][p%self.size] = 0

        numSize = len(str(self.size))

        self.printPuzzleBoard(numSize)

    def printPuzzleBoard(self, numSize):
        print("\n")
        for line in self.board:
            print("["+"  ".join(f"{n or '0':{numSize}}" for n in line)+"]")
        print("\n")

def shuffle(s):
    return sample(s,len(s))
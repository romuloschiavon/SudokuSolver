from random import sample

class Board():
    def __init__(self, base, square):
        self.base = base
        self.size = base*base
        self.square = square
        self.board = self.createPuzzleBoard()

    def pattern(self, r, c): 
        return (self.base*(r%self.base)+r//self.base+c)%self.size

    def createSolutionBoard(self):
        rangeBase = range(self.base)
        rows = [g*self.base + r for g in shuffle(rangeBase) for r in shuffle(rangeBase)]
        columns = [g*self.base + c for g in shuffle(rangeBase) for c in shuffle(rangeBase)]
        nums = shuffle(range(1, self.size+1))

        self.board = [[nums[self.pattern(r=r,c=c)] for c in columns] for r in rows]

        #if self.print:
        #    self.printSolutionBoard()

    #def printSolutionBoard(self):
    #    for line in self.board:
    #        print(line)

    def createPuzzleBoard(self):
        self.createSolutionBoard()
        #square = self.size * self.size
        zeros = self.square * 3//4
        for p in sample(range(self.square), zeros):
            self.board[p//self.size][p%self.size] = 0
        
        #if self.print:
        #    self.printPuzzleBoard()
        return self.board

    #def printPuzzleBoard(self):
    #    numSize = len(str(self.size))
    #    for line in self.board:
    #        print("["+"  ".join(f"{n or '0':{numSize}}" for n in line)+"]")

def shuffle(s):
    return sample(s,len(s))
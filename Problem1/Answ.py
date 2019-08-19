from itertools import permutations

class Answ():
    def __init__ (self, array, targ):
        self.array = array
        self.targ = targ
    def checkArray(self):
        sol = [pair for pair in permutations(self.array, 2) if sum(pair) == self.targ]
        return sol != None

answ = Answ([10, 15, 3, 7], 17)
sol = answ.checkArray()
print(sol)
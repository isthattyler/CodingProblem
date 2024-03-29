class Answ():
    def __init__ (self, array, targ):
        self.array = array
        self.targ = targ
    def checkArray(self):
        seen = {}
        for i in self.array:
            diff = self.targ - i
            if i in seen:
                return True
            seen[diff] = i
        return False

answ = Answ([10, 15, 3, 7], 15)
sol = answ.checkArray()
print(sol)

# This runs in O(n), where it uses dictionary to store value
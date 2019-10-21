class Solution:
    def __init__(self, arr):
        self.array = arr

    def productExceptSelf(self):
        length = len(self.array)
        answer = [0]*length
        answer[0] = 1
        temp = 1;

        for i in range(1, length):
            answer[i] = self.array[i - 1] * answer[i - 1]

        for i in reversed(range(length)):
            answer[i] = answer[i] * temp
            temp *= self.array[i]
        return answer

    def productExceptSelfSlow(self): # O(n^2)
        sol = []
        for i in self.array:
            temp = 1
            for j in self.array:
                if not (i == j):
                    temp *= j
            sol.append(temp)
        return sol

sol = Solution([1, 2, 3, 4, 5])
a = sol.productExceptSelf()
b = sol.productExceptSelfSlow()
print(a)
print(b)
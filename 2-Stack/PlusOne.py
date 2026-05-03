class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numStr = ""
        for digit in digits:
            numStr += str(digit)
        num = int(numStr) + 1
        numStr = str(num)
        digitsPlusOne = [0] * len(numStr)
        for i in range(len(digitsPlusOne)):
            digitsPlusOne[i] = int(numStr[i])
        return digitsPlusOne    

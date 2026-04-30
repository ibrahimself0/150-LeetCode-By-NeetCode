
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        newNum = n
        
        while True:
            digit_sum = 0
            for digit_char in str(newNum):
                digit_sum += int(digit_char) * int(digit_char)
            
            newNum = digit_sum
            
            if digit_sum == 1:
                return True
            elif digit_sum in seen:
                return False
            
            seen.append(digit_sum)
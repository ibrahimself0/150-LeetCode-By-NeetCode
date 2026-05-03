class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for char in s:
            if char.isalnum():
                result.append(char)
        result =  ''.join(result)
        print(result)
        return result.lower() == result[::-1].lower()

s = Solution()
print(s.isPalindrome("Was it a car or a cat I saw?"))
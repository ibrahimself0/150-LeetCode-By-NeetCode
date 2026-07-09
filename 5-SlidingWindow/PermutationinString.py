class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        left = 0

        for right, char in enumerate(s2):
            window[char] += 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                left += 1

            if window == need:
                return True

        return False       


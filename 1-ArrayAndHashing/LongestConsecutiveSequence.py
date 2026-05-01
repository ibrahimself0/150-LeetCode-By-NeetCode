class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if(len(nums) == 0):
            return 0
        sortedNums = sorted(list(set(nums)))
        Consecutives = []
        x = 1
        for i in range(len(sortedNums) - 1):
            if(sortedNums[i] - sortedNums[i+1] == -1):
                x = x + 1
            else :
                Consecutives.append(x)
                x = 1
        Consecutives.append(x)        
        return max(Consecutives)        

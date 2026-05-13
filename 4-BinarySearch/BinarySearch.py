class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = int(len(nums)/2)
        while i < len(nums) and i > 0:
            if(nums < i):
                i = i - 1
        
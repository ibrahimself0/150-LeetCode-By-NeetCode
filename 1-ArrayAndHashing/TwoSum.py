class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        xTraget = target
        for i in range(len(nums)):
            xTraget = xTraget - nums[i]
            for j in range(len(nums)):
                if i != j and xTraget - nums[j] == 0:
                    return [i,j]
            xTraget = target        
                    
            

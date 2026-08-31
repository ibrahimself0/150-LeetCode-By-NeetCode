class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0 , len(nums) -1
        while (l<=r):
            m = (l + r)//2
            if(target < nums[m]):
                r = m - 1
            elif(target > nums[m]):
                l = m  + 1 
            else:
                return True 

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if(self.search(arr,target)):
                return True
        else:
            return False
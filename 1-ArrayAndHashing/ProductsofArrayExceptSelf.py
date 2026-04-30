class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= []
        x = 1
        counter = Counter(nums)

        if(counter[0] > 1):
            return [0] * len(nums)

        for num in nums:
            x = x*num

        for num in nums:

            if num == 0:
                y = 1
                for num in nums:
                    if num == 0:
                        continue 
                    y = y*num
                res.append(int(y))
                continue     

            res.append(int(x/num))    
            
        return res     
            
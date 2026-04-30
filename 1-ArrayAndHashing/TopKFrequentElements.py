from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) 
        res = []
    
        for num, freq in counter.most_common(k):
            res.append(num)
        return res

s = Solution()
print(s.topKFrequent([7,7], 2))
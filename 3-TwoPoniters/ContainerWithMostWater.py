class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights) - 1
        j = 0
        maxA = 0
        while n > 0 and j < len(heights) - 1:   

            tempArea = 0

            if(heights[n]>heights[j]):
                tempArea = heights[j] * (n-j)

            else:
                tempArea = heights[n] * (n-j)

            if(tempArea > maxA):
                maxA = tempArea
            if(heights[n]>=heights[j]):
             j+=1
            else:
             n-=1     
        return maxA               

        
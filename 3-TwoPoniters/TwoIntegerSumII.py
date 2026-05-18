class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        sortedList = sorted(numbers)
        n = len(numbers) - 1
        j = 0
        while n > 0 and j < len(numbers) - 1:
            print(sortedList[j], sortedList[n])
            if(sortedList[j] + sortedList[n] == target):
                return [sortedList[j],sortedList[n]] 
            elif(sortedList[j] + sortedList[n] < target):
                j +=1
            else:
                n-=1;
s =Solution()
print(s.twoSum([1,2,3,4],3))
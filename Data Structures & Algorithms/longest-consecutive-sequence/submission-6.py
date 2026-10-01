class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        numSet = set()
        count = 1


        for num in nums:   #O(n)
            numSet.add(num)
        
        for num in numSet:
            if num -1 not in numSet: #the num is the start of the sequence
                j = 1
                tempCount = 1
                while num + j in numSet:
                    tempCount += 1
                    j+=1
                if tempCount > count:
                    count = tempCount
            
        return count

        
        

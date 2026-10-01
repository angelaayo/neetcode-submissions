class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        numSet = set(nums)
        count = 1
        
        for num in numSet:
            if num -1 not in numSet: #the num is the start of the sequence
                j = 1
                while num + j in numSet:
                    j+=1
                count = max(count, j)
        return count

        
        

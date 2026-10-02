class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mIdx = (left+right)//2
            res = min(res, nums[mIdx])
            if nums[mIdx] >= nums[left]:
                left = mIdx+1
            else:
                right = mIdx-1
        return res
            

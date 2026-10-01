class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mIdx = (left + right)//2
            if nums[mIdx] == target:
                return mIdx
            elif nums[mIdx] < target:
                left = mIdx +1
            elif nums[mIdx] > target:
                right = mIdx -1

        return -1
            
        
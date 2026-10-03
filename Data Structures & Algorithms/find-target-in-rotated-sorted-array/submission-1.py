class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1


        while left <= right:
            mIdx = (left+right)//2
            if nums[mIdx] == target:
                return mIdx
            # left sorted portion:
            if nums[left] <= nums[mIdx]:
                if target > nums[mIdx] or target < nums[left]:
                    left = mIdx+1
                else:
                    right = mIdx-1

            else:
                if target < nums[mIdx] or target > nums[right]:
                    right = mIdx -1
                else:
                    left = mIdx+1
        return -1




        
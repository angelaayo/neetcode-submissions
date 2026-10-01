class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, nums in enumerate(nums):
            if nums == target:
                return idx
        return -1
        
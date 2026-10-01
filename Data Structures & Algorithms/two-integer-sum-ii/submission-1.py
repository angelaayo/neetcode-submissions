class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seenNums = {}

        for idx, num in enumerate(numbers, start=1):
            diff = target - num
            if diff in seenNums:
                return [seenNums[diff], idx]
            else:
                seenNums[num] = idx
        
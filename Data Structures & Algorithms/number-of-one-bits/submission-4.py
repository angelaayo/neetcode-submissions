class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # odd numbers always have a right most bit of 1
        # hence the result of an odd number bit AND 1(0001)
        # is always 1
        while n:
           count += 1 if n & 1 else 0
           #then you shift the bit to the right by 1 to divide by 2
           n//=2
        return count
        
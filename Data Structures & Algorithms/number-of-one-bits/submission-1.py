class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            res = n % 2 
            if res == 1:
                count+=1
            n//=2
        return count
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #perform binary search over the range of possible eating
        # rates where the max here will be the max value in the pile
        left, right = 1, max(piles)
        res = 0

        while left <= right:
            mIdx = (left+right)//2
            count = 0
            for pile in piles:
               count+= math.ceil(float(pile)/mIdx)
            if count <= h:
                res = mIdx
                right = mIdx-1
            elif count > h:
                left = mIdx+1
        return res



        
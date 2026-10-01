class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need a high width which is determined by their distance
        #and a high height
        # determined by the minimum of their values
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            area = (right - left) * (min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            if res < area:
                res = area

        return res
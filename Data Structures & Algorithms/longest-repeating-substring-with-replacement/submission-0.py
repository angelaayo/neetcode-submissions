class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        countMap  = {}
        right = 0

        while right <= len(s)-1:
            countMap[s[right]] = 1 + countMap.get(s[right], 0)
            if not (((right-left)+1) - max(countMap.values()) <= k):
                #shift one value off to fix the window
                countMap[s[left]] = countMap.get(s[left],0) - 1
                left+=1
            right+=1
        return (right-left)
            

        
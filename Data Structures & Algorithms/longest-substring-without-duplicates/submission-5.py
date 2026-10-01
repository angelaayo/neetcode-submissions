class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenSet = set()
        maxLength = 0
        left = 0
        for right in range(len(s)):
            if s[right] in seenSet:
                while s[right] in seenSet:
                    seenSet.remove(s[left])
                    left+=1
            seenSet.add(s[right])
            maxLength = max(maxLength, len(seenSet))
        return maxLength


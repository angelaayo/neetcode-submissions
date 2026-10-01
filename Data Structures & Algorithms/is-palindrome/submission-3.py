class Solution:
    def isPalindrome(self, s: str) -> bool:
        newArray = []
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            newArray.append(s[i].lower())
        right= len(newArray)-1
        for i in range(len(newArray)//2):
            if newArray[i] != newArray[right]:
                return False
            right-=1
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        stringS = {}
        stringT = {}
        for i, char in enumerate(s):
            #create a hashmapping to each char then compare them
            stringS[s[i]] = 1 + stringS.get(s[i], 0)
            stringT[t[i]] = 1 + stringT.get(t[i], 0)
        return stringS == stringT  


        
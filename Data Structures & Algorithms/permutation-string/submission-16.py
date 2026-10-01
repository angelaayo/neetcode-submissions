class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Array = [0] * 26
        s2Array = [0] * 26

        for i in range(len(s1)):
            s1Array[ord(s1[i]) - ord('a')]+=1


        for j in range(len(s1)):  #build the hashMap for the first len(s1) char of s2 to start the window
            s2Array[ord(s2[j]) - ord('a')]+=1
        
        left = 0
        right = len(s1)-1

        while right < len(s2):  
            if s1Array == s2Array:
                return True
            elif right+1 < len(s2):
                s2Array[ord(s2[left]) - ord("a")]-=1 
                s2Array[ord(s2[right + 1]) - ord("a")]+=1 
            left+=1
            right+=1
        return False
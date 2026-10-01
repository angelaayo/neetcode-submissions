class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countMap = {}

        for i in range(len(s1)):
            countMap[s1[i]] = 1 + countMap.get(s1[i], 0)
        
        left = 0
        right = len(s1)-1

        while right in range(len(s2)):
            tempHashmap = {}
            i = 0
            start = left
            end = right
            while start <= end:     #l e cab   ee
                tempHashmap[s2[start]] = 1 + tempHashmap.get(s2[start], 0)
                start+=1
            if tempHashmap == countMap:
                return True
            left+=1
            right+=1
        return False


        
        
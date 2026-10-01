class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        countMap = {}
        countS2Map = defaultdict(int)

        for i in range(len(s1)):
            countMap[s1[i]] = 1 + countMap.get(s1[i], 0)   #a-1 b-1


        for j in range(len(s1)):  #build the hashMap for the first len(s1) char of s2 to start the window
            countS2Map[s2[j]] = 1 + countS2Map.get(s2[j], 0)
        
        left = 0
        right = len(s1)-1

        while right < len(s2):  
            if countMap == countS2Map:
                return True
            elif right+1 < len(s2):
                countS2Map[s2[left]]-=1 
                if countS2Map[s2[left]] == 0:
                    del countS2Map[s2[left]]
                countS2Map[s2[right+1]]+=1
            left+=1
            right+=1
        return False
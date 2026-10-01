class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0: return ""
        enResult = ""
        #say we have [me#., 3.and, 1my1, face]
        #    4.me#.5.3.and4.1my14.face
        #3 . me#5 .3.and 4.1my14.face
        #so we need the count of how many characters
        #in the string and we use that followed
        # by a period to build our result
        for string in strs:
            count = len(string)
            enResult+= str(count) + "." + string
        return enResult


    def decode(self, s: str) -> List[str]:
        if len(s) <=0: return []
        deResult = []
        i = 0
        count = 0
        while i < len(s):
            if s[i] != ".":
                count = count * 10 + int(s[i])
                i+=1
                continue
            string = ""
            # for j in range(count):
            #     string+=(s[i+1+j])
            string+= s[i+1: i+count+1]
            i+=count+1
            count = 0
            deResult.append(string)
        return deResult
        
            


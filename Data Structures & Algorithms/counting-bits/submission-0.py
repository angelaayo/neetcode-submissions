class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        count = 0
        for i in range(len(output)):
            j = i
            while j > 0:
                count += 1 if j & 1 else 0
                j//=2
            output[i] = count
            count = 0
        return output

        
        
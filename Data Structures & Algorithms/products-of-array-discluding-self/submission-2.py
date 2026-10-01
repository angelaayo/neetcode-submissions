class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIdx = [] #keep track of where the zeros are
        product = 1
        result = []
        for idx, num in enumerate(nums):
            if num == 0:
                zeroIdx.append(idx)
                if len(zeroIdx) > 1:
                    return [0] * len(nums)
            else:
                product*=num
        
        #now we should have the product goal
        for idx, num in enumerate(nums):
            if num == 0:
                result.append(product)
            elif len(zeroIdx) == 1:
                result.append(0)
            else:
                result.append(product//num)
        return result
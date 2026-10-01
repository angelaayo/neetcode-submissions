class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we need to find all possible combinations
        #at each index that sums up to 0
        #with 2 other values in the array
        # then if we come across that value again we
        #skip it
        #[-4,-1,-1,0,1,2]
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i +1
            right = len(nums)-1
            if i !=0 and (nums[i] == nums[i-1]):
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    #too big we need to decrease from the right
                    right-=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    #too small we need to grow by increasing left
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    #in the case the next numbers are still the same:
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return result

                

        
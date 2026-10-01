class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #for this approach we can start with the middle array
        # and if the last number is greater than the target and
        # the first number is lower than our target is in there
        # else if the last number is less then we eliminate that array
        #and every array before it
        #else if the last number is higher and the first is also higher
        #then we eliminate that array and everything that comes after it

        left = 0
        right = len(matrix)-1
        while left <= right:
            mIdx = (right+left)//2
            mArray = matrix[mIdx]
            if mArray[len(mArray) -1] < target:
                left = mIdx+1
            elif mArray[len(mArray)-1] > target and mArray[0] > target:
                right = mIdx-1
            else:   #perform binary search here too
                left = 0
                right = len(mArray)-1
                while left <= right:
                    mIdx = (right+left)//2
                    if mArray[mIdx] == target:
                        return True
                    elif mArray[mIdx] < target:
                        left = mIdx+1
                    else:
                        right = mIdx-1
                return False
        return False


            # [0,1,2,3,4,5,6,7,8,9]  5 6 7 8 9
                

        
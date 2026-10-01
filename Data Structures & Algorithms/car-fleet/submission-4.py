class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 + 3n = 10  (target - pos)/speed

        pair = [(pos, speed) for pos, speed in zip(position, speed)] #put the two arrays tgether
        pair.sort(reverse=True) #sorted in descending order based on position
        stack = []  # stores the time taken   (4,1)(2,3)(0,2)

        for pos, speed in pair:
            timeTaken = (target - pos)/speed   #stack   =  8/3   
            if stack and stack[-1] >= timeTaken:
                continue
            else:
                stack.append(timeTaken)
        return len(stack)


        
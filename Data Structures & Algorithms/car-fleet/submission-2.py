class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1 + 3n = 10  (target - pos)/speed
        # so the idea here is we compare the time it takes for the fleets to reach the
        # destination in order so the highest will be at the top of the stack
        # if the next reaches it before then we pop the stack and add the next
        #then we compare the one behind the second to the second and if it catches up
        # then we also pop the second if it doesnt then we simply append that to the
        # stack and that operates as our new top

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


        
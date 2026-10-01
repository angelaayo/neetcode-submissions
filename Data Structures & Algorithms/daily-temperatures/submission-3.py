class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack to store the days not logged
        #each time we come across a day we check if theres one already in the stack
        # that doesnt have a next if so we pop it
        #30 push it...top: 30    [30, 28, 38, 36, 35, 40, 28] = [2,1,3,2,1,0,0]
        #then we have 28 which is less than we add it to the stack top: 28
        # then we have 38 which is greater than the top so while 38 is greater
        # we pop the top and calculate that distance
        #so in this case 28 and 30 are popped and we have [2,1] then 38 is added top = 38
        #then we get to 36 its not greater so we add it now the top is 36.....38,36
        #then we get to 35 which is also not greater so we add it 38,36,
        #then we get to 40 which is greater so while its greater than the top we calc distance and pop
        #[2,1,3,2,1]

        res = [0] * len(temperatures)
        stack = [] #[index, temp]
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                res[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            stack.append([idx, temp])
        return res

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posTime = []
        for i in range(len(position)):
            posTime.append([position[i], speed[i]])

        posTime.sort(reverse=True)

        stack = []
        for i in range(len(posTime)):

            time = (target - posTime[i][0]) / posTime[i][1]

            if stack: 
                if time > stack[-1]:
                    stack.append(time)
            else: 
                stack.append(time)

        return len(stack)
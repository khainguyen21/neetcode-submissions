class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSped = []
        for i in range(len(position)):
            posSped.append([position[i], speed[i]])
        
        posSped.sort(reverse=True)
        stack = []

        for i in range(len(posSped)):
            time = (target - posSped[i][0]) / posSped[i][1]
            if stack and time <= stack[-1]: 
                continue

            stack.append(time)

        return len(stack)
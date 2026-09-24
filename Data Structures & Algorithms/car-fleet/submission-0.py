class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        startPos = []

        for i in range(len(position)):
            startPos.append([position[i], speed[i]])

        # Python's default sorting behavior is to look at the first element
        # of each sub-list (each car) to determine the order.
        startPos.sort(reverse = True)

        stackTime = []
        for i in range(len(startPos)):
            time = ( target - startPos[i][0] ) / startPos[i][1]
            
            if stackTime: 
                if time > stackTime[-1]:
                    stackTime.append(time)
            else: 
                stackTime.append(time)

        return len(stackTime)
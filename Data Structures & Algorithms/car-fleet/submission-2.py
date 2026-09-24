class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        startPos = []

        for i in range(len(position)):
            startPos.append([position[i], speed[i]])

        # Python's default sorting behavior is to look at the first element
        # of each sub-list (each car) to determine the order.
        startPos.sort(reverse = True)

        fleet = 0
        prevTime = 0

        for i in range(len(startPos)):
            currentTime = ( target - startPos[i][0] ) / startPos[i][1]
            
            if fleet != 0: 
                if currentTime > prevTime:
                    fleet += 1
                    prevTime = currentTime
            else:
                fleet += 1
                prevTime = currentTime

        return fleet
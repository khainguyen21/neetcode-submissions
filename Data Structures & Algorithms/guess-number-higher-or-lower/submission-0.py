# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0

        while l <= n: 
            guessNum = (l + n) // 2

            if guess(guessNum) > 0: 
                l = guessNum + 1

            elif guess(guessNum) < 0: 
                n = guessNum - 1

            else: 
                return guessNum
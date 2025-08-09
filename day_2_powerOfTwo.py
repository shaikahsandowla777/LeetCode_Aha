#Leetcode 231-Power of 2 (Easy)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 #1 line answer

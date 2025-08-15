class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0
        # (All powers of two are positive; zero and negative numbers are not valid)
        # Then use bitwise AND to check if n has only one bit set to 1
        # A number that is a power of two has a binary representation like: 1000, 100, 10, etc.
        # n - 1 will flip all the bits after the first set bit (including it)
        # So, for powers of two: n & (n - 1) == 0
        # Example: 8 -> 1000, 7 -> 0111, 1000 & 0111 == 0000
        return n > 0 and (n & (n - 1)) == 0

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0           # Total number of zero-filled subarrays
        zero_streak = 0     # Current count of consecutive zeros

        for num in nums:
            if num == 0:
                # Extend the current streak of zeros
                zero_streak += 1
                # Add the number of new subarrays ending at this zero
                # For each zero in the streak, a new subarray ends here
                count += zero_streak
            else:
                # Reset the streak if the number is not zero
                zero_streak = 0

        return count

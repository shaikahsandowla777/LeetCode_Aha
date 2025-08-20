class Solution:
    def judgePoint24(self, nums: list[int]) -> bool:
        EPSILON = 1e-6
        TARGET = 24
        
        def helper(arr):
            # If only one number left, check if it equals 24 within tolerance
            if len(arr) == 1:
                return abs(arr[0] - TARGET) < EPSILON
            
            # Try all pairs of numbers
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if i != j:
                        # Create a new list excluding i and j
                        new_arr = [arr[k] for k in range(len(arr)) if k != i and k != j]
                        
                        # Possible results of operations on arr[i] and arr[j]
                        a, b = arr[i], arr[j]
                        candidates = [a + b, a - b, b - a, a * b]
                        
                        # Avoid division by zero
                        if abs(b) > EPSILON:
                            candidates.append(a / b)
                        if abs(a) > EPSILON:
                            candidates.append(b / a)
                        
                        # For each candidate, recurse with the new array plus candidate
                        for val in candidates:
                            if helper(new_arr + [val]):
                                return True
            
            return False
        
        return helper(nums)

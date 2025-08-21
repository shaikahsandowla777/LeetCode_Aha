class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])  # m = number of rows, n = number of columns

        # Step 1: Convert matrix into histogram of consecutive 1s vertically.
        # For each cell, if it is 1, increase the count by the value directly above it.
        # This tells us how tall the column of 1s is at each cell.
        for i in range(1, m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]

        total = 0  # This will store the final count of submatrices

        # Step 2: For each row (which now represents histogram heights), count rectangles
        for row in mat:
            stack = []         # Monotonic increasing stack to help with rectangle counting
            count = [0] * n    # count[j] = number of submatrices ending at column j
            for j in range(n):
                # Maintain the stack such that the heights are strictly increasing
                while stack and row[stack[-1]] >= row[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]  # Index of previous smaller height
                    # Number of new rectangles ending at column j:
                    #   - row[j]: height
                    #   - (j - prev): width of new segment
                    #   - count[prev]: rectangles ending at prev
                    count[j] = count[prev] + row[j] * (j - prev)
                else:
                    # No smaller height to the left, so all submatrices end here
                    count[j] = row[j] * (j + 1)

                stack.append(j)      # Add current column index to stack
                total += count[j]   # Add to the total count

        return total

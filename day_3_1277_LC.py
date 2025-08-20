class Solution:
    def countSquares(self, matrix):
        # Get the dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize the counter for total square submatrices
        count = 0

        # Iterate over every cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Only process cells that are 1 (possible bottom-right of a square)
                if matrix[i][j] == 1:
                    # For all cells not in the first row or first column,
                    # compute the size of the largest square ending here
                    if i > 0 and j > 0:
                        # Take the min of (top, left, top-left) neighbors and add 1
                        matrix[i][j] = 1 + min(
                            matrix[i-1][j],     # top
                            matrix[i][j-1],     # left
                            matrix[i-1][j-1]    # top-left
                        )
                    # Add the square count ending at this cell to the total
                    count += matrix[i][j]

        # Return the total number of square submatrices
        return count

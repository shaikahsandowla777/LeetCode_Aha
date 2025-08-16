class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the input number to a string so we can manipulate its digits
        # Example: 9669 -> "9669"
        num_str = str(num)
        
        # Use the string replace() function to change the first occurrence of '6' to '9'
        # The third argument '1' ensures that only the first '6' is replaced
        # Example: "9669".replace('6', '9', 1) -> "9969"
        max_num_str = num_str.replace('6', '9', 1)
        
        # Convert the modified string back to an integer
        # Example: "9969" -> 9969
        return int(max_num_str)

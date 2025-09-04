import sys

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) < abs(y-z):
            return 1
        elif abs(z-x) > abs(y-z):
            return 2
        return 0



### DRIVER CODE (later replaced by runner.py)
# # The following code handles the input/output for the task.
# if __name__ == "__main__":
#     input_values = sys.stdin.readline().split()
#     if len(input_values) == 3:
#         x = int(input_values[0])
#         y = int(input_values[1])
#         z = int(input_values[2])
        
#         solution = Solution()
#         result = solution.findClosest(x, y, z)
#         print(result)
#     else:
#         print("Error: Expected exactly three integer inputs.")

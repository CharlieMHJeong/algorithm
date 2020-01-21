class Solution:
    # def trap(self, height: List[int]) -> int:
    def trap(self, height):
        if not height:
            return 0
        # set n for the length of the list "height"
        n = len(height)
        # set left_max list the same length of the
        left_max, right_max = [0] * n, [0] * n

        # scan from left to right to find the highest left edge
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])

        #Scan from right to left to find the highest edge to the right of each position
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        #Scan each position, using the shortest left and right sides of the current position as the length,
        # and subtract the value of the current position to obtain the capacity of the current position
        res = 0
        for i in range(1, n-1):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
#LeftMax: [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
#RigthMax: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
height = [0,1,0,2,1,0,1,3,2,3,2,1]
s = Solution()
r = s.trap(height)
print(r)
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height))

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution:
    def twoSum(self, nums, target) :
        d = {}
        for i, num in enumerate(nums):
            gap = target - num
            if gap not in d:
                d[num] = i
            else:
                return [d[gap], i]
        print(d)


s = Solution()
r = s.twoSum([11,2,15,7], 9)
print(r)

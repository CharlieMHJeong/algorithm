class Solution:
    def removeElement(self, nums, val):

        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)


s = Solution()
r = s.removeElement([0,1,2,2,3,0,4,2],2 )
print(r)

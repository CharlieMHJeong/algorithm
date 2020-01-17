class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        end = len(nums)
        read = 1
        write = 1
        while read < end:
            if nums[read] != nums[read -1]:
                nums[write] = nums[read]
                write +=1
            read +=1
        return write



s = Solution()
r= s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(r)

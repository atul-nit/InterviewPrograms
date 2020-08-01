class Solution:
    def removeDuplicates(self, nums: list) -> int:
        res = nums[:]
        for i in range(len(res) - 1):
            currentval = res[i]
            nextval = res[i + 1]
            if currentval == nextval:
                nums.remove(currentval)
        return len(nums)




nums = [1,1,2,3,3,3,4]
s = Solution()
l = s.removeDuplicates(nums)
aa = nums[:l] # nums[0:4]
print(aa)

"""
nums = [1,1,2,3,3,3,4]
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev_sum = 0
        for idx, i in enumerate(nums):
            prev_sum += i
            nums[idx] = prev_sum
        
        return nums

solution = Solution().runningSum([1,2,3,4])
print(solution)
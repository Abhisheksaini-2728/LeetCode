class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_end = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            v1 = best_end + nums[i]
            v2 = nums[i]

            best_end = max(v1,v2)
            result = max(result,best_end)

        return result    
        
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]

        max_res = nums[0]
        min_res = nums[0]

        for i in range(1,len(nums)):
            v1 = max_num + nums[i]
            v2 = min_num + nums[i]
            v3 = nums[i]

            max_num = max(v1,v3)
            min_num = min(v2,v3)

            max_res = max(max_res,max_num)
            min_res = min(min_res,min_num)

        return max(max_res,abs(min_res))    
        
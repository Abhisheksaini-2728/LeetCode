class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_end = nums[0]
        min_end = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            v1 = max_end * nums[i]
            v2 = min_end * nums[i]
            v3 = nums[i]

            max_end = max(v1,v2,v3)
            min_end = min(v1,v2,v3)

            ans = max(ans,max_end,min_end)
        return ans    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_num = 0
        result = float("inf")
        left = 0

        for right in range(len(nums)):
            sum_num = sum_num + nums[right]

            while sum_num >= target:
                result = min(result,right - left + 1)

                sum_num = sum_num - nums[left]
                left += 1

        if result == float("inf"):
            return 0        

        return result        


        
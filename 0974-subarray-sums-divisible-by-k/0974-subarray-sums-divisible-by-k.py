class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        sum = 0
        ans = 0
        dict_num = {0:1}

        for i in range(len(nums)):
            sum += nums[i]

            rem  = sum % k

            if rem < 0:
                rem = rem + k

            if rem in dict_num:
                ans += dict_num[rem]

            if rem in dict_num:
                dict_num[rem] += 1

            else:
                dict_num[rem] = 1

        return ans
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       prefix = 0
       count = 0
       dict_num = {0:1}

       for i in nums:
        prefix += i

        if prefix - k in dict_num:
            count += dict_num[prefix - k]

        if prefix in dict_num:
            dict_num[prefix] += 1

        else:
            dict_num[prefix] = 1     
    
       return count

       
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_power = arr[0]
        power = 0
        res = arr[0]

        for i in range(1,len(arr)):
            v1 = arr[i]
            v2 = no_power + arr[i]
            v3 = power + arr[i]
            v4 = no_power

            no_power = max(v1,v2)
            power = max(v3,v4)

            res = max(res,no_power,power)
        
        return res     
        
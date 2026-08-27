class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        low = 0
        high = 0
        res = 0
        count = 0
        sum = 0

        for high in range(k):
            sum += arr[high]

        while high < len(arr):
            if (sum / k) >= threshold:
                count += 1

            res = max(res,count)
            low += 1
            high += 1

            if high == len(arr):
                break

            sum = sum - arr[low - 1] + arr[high]

        return res                

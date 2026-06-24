class Solution:
    def threeSumClosest(self, nums,target):
        nums.sort()

        diff_inf = float("inf")
        result = 0

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)

                if diff < diff_inf:
                    diff_inf = diff
                    result = total

                elif total == target:
                    return result    

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return result                 
        
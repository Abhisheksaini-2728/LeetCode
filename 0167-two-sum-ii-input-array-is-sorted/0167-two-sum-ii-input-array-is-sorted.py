class Solution: 
    def twoSum(self,list_num,target):
        list_num.sort()

        left = 0
        right = len(list_num)-1

        while left < right:
            item = list_num[left] + list_num[right]

            if item == target:

                return [left + 1 , right + 1]

            elif item > target:

                right -= 1

            else:
                left += 1

        return []

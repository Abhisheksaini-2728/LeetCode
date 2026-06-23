class Solution:
    def removeDuplicates(self, list_num):
        left = 0
        right = 1

        while right < len(list_num):
            
            if list_num[left] != list_num[right]:
                left += 1
                list_num[left] = list_num[right]

            right += 1    
        
        return left + 1
        
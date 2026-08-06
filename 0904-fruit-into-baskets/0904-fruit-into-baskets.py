class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        result = 0
        dict_str = {}

        for right in range(len(fruits)):
            if fruits[right] not in dict_str:
                dict_str[fruits[right]] = 1
            else:
                dict_str[fruits[right]] += 1

            while len(dict_str) > 2:
                dict_str[fruits[left]] -= 1
                
                if  dict_str[fruits[left]] == 0:
                    del dict_str[fruits[left]]

                left += 1

            result = max(result,right - left + 1)   

        return result         

            
        
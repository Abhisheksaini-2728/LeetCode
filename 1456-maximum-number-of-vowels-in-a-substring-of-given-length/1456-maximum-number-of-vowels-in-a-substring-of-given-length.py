class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        low = 0
        high = 0
        res = 0
        count = 0

        for high in range(k):
            if s[high] in "aeiou":
                count += 1

        while high < len(s):
            res = max(res,count)
            low += 1
            high += 1

            if high == len(s):
                break

            if s[low - 1] in "aeiou":
                count -= 1

            if s[high] in "aeiou":
                count += 1

        return res                         
        
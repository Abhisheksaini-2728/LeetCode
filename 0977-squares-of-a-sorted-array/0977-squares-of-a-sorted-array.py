class Solution:
    def sortedSquares(self, list_num):

        a = []
        b = []

        # Split into non-negative and negative
        for num in list_num:
            if num >= 0:
                a.append(num)
            else:
                b.append(num)

        # Square positive part
        for i in range(len(a)):
            a[i] = a[i] * a[i]

        # Square negative part
        for i in range(len(b)):
            b[i] = b[i] * b[i]

        # Negative squares reverse karo
        b.reverse()

        # Merge two sorted arrays
        result = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):

            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        while i < len(a):
            result.append(a[i])
            i += 1

        while j < len(b):
            result.append(b[j])
            j += 1

        return result
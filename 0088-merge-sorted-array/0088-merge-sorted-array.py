class Solution:
    def merge(self, nums1,m,nums2,n):
        list1 = nums1[:m]
        list2 = nums2[:n]
        i = 0
        j = 0
        result = []

        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1

            else:
                result.append(list2[j])
                j += 1

        while i < len(list1):
            result.append(list1[i])
            i += 1

        while j < len(list2):
            result.append(list2[j])
            j += 1

        for k in range(len(result)):
            nums1[k] = result[k]

        return nums1                        
        
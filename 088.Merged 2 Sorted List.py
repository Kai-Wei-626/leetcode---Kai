class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # i is the pointer to nums1
        # j is the pointer to nums2
        for x in reversed(range(len(nums1))):
            if m <= 0:
                for k in range(n):
                    nums1[k] = nums2[k]
                break
            if n <= 0:
                break

            if nums1[m-1] > nums2[n-1]:
                nums1[x] = nums1[m-1]
                m = m - 1
            else:
                nums1[x] = nums2[n-1]
                n = n - 1

            
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] =  nums1[m-1]
                m = m - 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]
            

            

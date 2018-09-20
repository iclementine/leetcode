"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

这道题目是要求求两个有序序列的中位数， 而且当数字的个数是偶数的时候， 是取中间两个数的均值而不是右侧的那个， 所以需要考虑比较细的边界条件。
如果二路归并， 则需要 O(m+n) 的时间， 这并不是最优的解法， 因为还没有利用数组的有序性。

因为邓老师的书上也有讲过， reduce and conquer 的方法， 中位数就是那些大于它和小于它的数的数量相等的数。或者是说在它的左侧和右侧的数的数量相等。
利用有序性， 可以先找出短的那个序列的中位数。然后它左侧 a 个数， 右侧 b 个数， 那么可以找出长的序列的左侧第 b+1 个数， 或者右数第 a+1 个数。然后比较这三个数，
可以一次过去掉很长的区间。
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        if n1 == 0:
            return self.find_median(nums2)
        return self.find_median_with_index(nums1, 0, n1, nums2, 0, n2)

        
    def find_median_with_index(self, nums1, lo1, s1, nums2, lo2, s2):
        # 这个接口是模仿邓老师的设计， 这样的带有 idx 的写法的好处在于， 把递归改成迭代（循环）的时候很直接， 如果递归就改变 idx 再调用自身
        # 如果循环就改变 idx 再执行一次, 而数据 array 本身可以一致不用改变， 在循环的写法这很自然， 而对于递归写法就比较好了。
        if s1 > s2:
            nums1, nums2, s1, s2, lo1, lo2 = nusm2, nums1, s2, s1, lo2, lo1
        while (s1 + 3 <= s2):
            # 如果二者长度相差比较大， 以至于短序列即使都比长序列小或者都比长序列大， 也不能把中位数拉到长序列的端点， 则直接截掉长序列的两侧
            
            lo2 += (s2 - s1 -1) // 2
            s2 -= ((s2 - s1 - 1) // 2) * 2
            
        while (s1 > 2):
            # 如果短序列长度不到3， 可能会出现某一侧是空， 酱紫会死循环
            if s1 > s2:
                nums1, nums2, s1, s2, lo1, lo2 = nums2, nums1, s2, s1, lo2, lo1 # 如果切着切着， 长短互换， 再换回来
            # 注意边界条件， 对于 n 是偶数 n // 2 是大侧的那个数， 对于奇数， 那就正好。无论奇数还是偶数， 左侧刚好 n//2 个数， 右侧则是 (n-1)//2 个数
            m1 = lo1 + s1 // 2
            m2a = lo2 + (s1 - 1) // 2
            m2b = lo2 + s2 - 1 - s1 // 2
            if nums1[m1] > nums2[m2b]:
                # larger， 去掉 nums1 的右侧， nums1 的左侧
                lo2 = m2a
                s2 -= (s1 - 1) // 2
                s1 -= (s1 - 1) // 2
            elif nums1[m1] < nums2[m2a]:
                # smaller， 去掉 nums1 的左侧， nums2 的右侧
                lo1 = m1
                s2 -= s1 // 2
                s1 -= s1 // 2
            else:
                # inside， 去掉 nums2 的两侧
                lo2 = m2a
                s2 -= ((s1-1) // 2) * 2
        return self.find_median(sorted(nums1[lo1:lo1+s1] + nums2[lo2:lo2+s2]))
        
                
    def find_median(self, nums):
        mib = len(nums) // 2
        if len(nums) % 2:
            return nums[mib]
        else:
            return (nums[mib -1] + nums[mib]) / 2

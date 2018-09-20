"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {} # residuals
        for i in range(len(nums)):
            if nums[i] not in res:
                res[target-nums[i]] = i # key: value, 余数 -> idx(ith 数值)
            else:
                j = res[nums[i]] # 如果 (ith 数值) 等于 (jth 数值) 的余数， 那么返回 (j,1) 
                break
        return j, i


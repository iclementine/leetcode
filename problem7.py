"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

经典的整数反转问题， 不需要转换成为列表。有一段经典的小代码
每次取出最后一位， 并且把源数字截掉一位，然后把之前的数字 * 10 + 取出的这一位
一次就可以完成反转
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        original = x
        if x < 0:
            x = -x
        
        m = 0
        while (x > 0):
            res = x % 10
            m = m * 10 + res
            x //= 10
        
        if original < 0:
            return -m if m <= 2 ** 31 else 0
        return m if m < 2 ** 31 else 0

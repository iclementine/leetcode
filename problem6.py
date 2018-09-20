"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

没有什么难度， 分析数字就可以了， 但是运行时间不好说
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        period = 2 * numRows - 2 # 周期， 比如说， 4行， 那么周期就是 6
        i = 0
        r = []
        while (i < numRows):
            # 直接找到每一行输出
            j = i # i 是行数， 一开始 j=i 就是第一列的第 i 行的 idx
            p1 = period - 2 * i # 一个步长
            p2 =  2 * i # 另一个步长
            while (j < len(s)):
                if p1 > 0:
                    r.append(s[j]) # 直接一个一个地 append
                    j += p1
                if (j < len(s)):
                    if p2 > 0:
                        r.append(s[j])
                        j += p2
            i += 1
        return ''.join(r)

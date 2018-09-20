"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

寻找最长回文子串， 著名的 Manacher 算法， 直接上
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = '#' + '#'.join(s) + '#' # 加上分隔符， 真是神来之笔

        p = [1]*len(t) # 以第 i 个字符为中心的最长回文子串的一半长度， 包含这个字符自身的长度， 因为用了 Manacher, 所以回文子串一定是奇数长度
        # 并且这个长度再 -1 就是这个回文子串的长度
        
        max_len = 1 # 最长回文子串的长度
        pos = 0 # 最长回文子串的中心位置
        
        for i in range(len(t)):
            if i < pos + max_len:
                p[i] = min(p[2 * pos - i], pos + max_len - i) # 最关键的一步， 利用 p 数组的对称性， 还在里面就对称
            else:
                p[i] = 1 # 超出了那就先记为 1
            while  i + p[i]  < len(t) and  i - p[i]  >= 0 and t[i - p[i]] == t[i + p[i]] :
                p[i] += 1 # 继续扩展， p[i] 在扩展， 直到不能扩展
            if p[i] > max_len:
                # 更新
                max_len = p[i]
                pos = i
        #print(t)
        #print(pos, p[pos])
        # return ''.join([x for x in t[pos - p[pos] + 1: pos + p[pos]] if x != '#'])
        start = pos // 2 - (p[pos] - 1) // 2
        return s[start: start + p[pos] -1]

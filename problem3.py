"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0 # 最长的无重复字符子串
        start = 0 # 以当前字符为结束字符的最长无重复子串的起始字符 idx
        span = 0 # 以当前字符为结束字符的最长无重复子串
        last_seen = {} # 字典， 用来存放每个字符上次见到的时候的 idx
        
        for i, c in enumerate(s):
            if c not in last_seen:
                last_seen[c] = i
                span += 1
            else:
                start = max(last_seen[c] + 1, start) # 如果这个字符已经出现过， 那么以这个字符为结束字符的子串最长可以回溯到这个字符上次出现的下一个字符， 如果中间已经有重复， 则回不到， 而值能够回到最右侧的那个 start. （也就是中间如果出现过重复了， 那就只能取那个字符为结束字符的最长子串起始点了）， 这一步是关键
                span = i - start + 1 # span 长度
                last_seen[c] = i # 
            if span > longest:
                longest = span # 更新 longest
        return longest


    #def lengthOfLongestSubstring(self, s):
        #dic, res, start, = {}, 0, 0
        #for i, ch in enumerate(s):
            #if ch in dic:
                #start = max(start, dic[ch]+1)
                #res = max(res, i-start+1)
            #else:
                #res = max(res, i-start+1)
            #dic[ch] = i
        #return res

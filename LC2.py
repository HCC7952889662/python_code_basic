
class Solution:

    def lengthOfLongestSubstring(self, s):
        unique_chars = []
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.append(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
        return longest

Input = "abcabcbb"

L = Solution().lengthOfLongestSubstring(Input)
print(L)

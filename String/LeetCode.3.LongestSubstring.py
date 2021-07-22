class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, current = "", ""
        for j in range(len(s)):
            i = current.find(s[j])
            if i >= 0:
                current = current[i + 1:]
            current += s[j]
            if len(longest) < len(current):
                longest = current[0:len(current)]
            print(longest, current)
        return len(longest)

sol = Solution()
# sin = "abcabcbb"
sin = "pwwkew"
print(sol.lengthOfLongestSubstring(sin))

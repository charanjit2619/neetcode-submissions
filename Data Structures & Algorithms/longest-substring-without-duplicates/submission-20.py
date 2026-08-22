class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0

        l, r = 0, 0

        seen = {}

        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
                longest = max(longest, r - l + 1)
            else:
                l = max(l, seen[s[r]] + 1)
                seen[s[r]] = r
                longest = max(longest, r - l + 1)
            
            r += 1

            
        return longest


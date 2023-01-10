class Solution:
    def lengthOfLongestSubstring(self, s):
        cnt = {}
        l, r = 0, 0
        mx = 0
        while r < len(s):
            if s[r] not in cnt:
                cnt[s[r]] = 1
                r += 1
            elif cnt[s[r]] == 0:
                cnt[s[r]] += 1
                r += 1
            else:
                cnt[s[l]] -= 1
                l += 1
            mx = max(mx, r - l)
        return mx

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(pre, cur)
                pre = cur
                cur = 1
            else: 
                cur += 1
        res += min(pre, cur)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # expend
            count[s[r]] = 1 + count.get(s[r], 0)

            # shrink
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
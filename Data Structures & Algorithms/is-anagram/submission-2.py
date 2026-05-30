class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = {}
        cnt2 = {}
        for i in range(len(s)):
            cnt[s[i]] = 1 + cnt[s[i]] if s[i] in cnt else 1
            cnt2[t[i]] = 1 + cnt2[t[i]] if t[i] in cnt2 else 1
        return cnt == cnt2
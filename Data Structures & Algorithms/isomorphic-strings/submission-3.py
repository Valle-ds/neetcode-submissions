class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}

        for i,z in zip(s,t):
            if (i in h1 and h1[i] != z) or (z in h2 and h2[z] != i):
                return False
            h1[i] = z
            h2[z] = i
        return True
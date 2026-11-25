class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n,m = 0, 0 
        for i in nums:
            if i == 0:
                n = max(n, m)
                m = 0
            else:
                m += 1
        return max(n, m)
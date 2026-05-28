class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        n = 0
        for i in nums:
            if i == 0:
                n = max(n,a)
                a = 0

            else:
                a += 1
        return max(n ,a )
        
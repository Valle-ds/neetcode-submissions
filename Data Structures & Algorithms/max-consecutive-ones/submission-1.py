class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        b = 0
        for i in nums:
            print(i, b)
            if i == 1:
                b += 1
                maximum = max(maximum, b)
            else:
                b = 0
        return maximum

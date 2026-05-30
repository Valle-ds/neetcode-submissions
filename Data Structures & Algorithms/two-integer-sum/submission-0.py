class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, z in enumerate(nums):
            d = target - z
            if d in h:
                return[h[d], i]
            h[z] = i
         

        
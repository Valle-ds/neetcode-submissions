class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[n] = nums[i]
            n += 1

        return n


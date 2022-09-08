class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_new = 0
        for i, num in enumerate(nums):
            if val != num:
                nums[next_new] = num
                next_new += 1
        return next_new

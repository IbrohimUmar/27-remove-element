class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_new = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[next_new] = nums[i]
                next_new += 1

        return next_new

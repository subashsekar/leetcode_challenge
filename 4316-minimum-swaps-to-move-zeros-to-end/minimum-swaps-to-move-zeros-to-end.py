class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero = nums.count(0)
        non_zero = len(nums)-zero
        swap =0
        for i in range(non_zero):
            if nums[i] == 0:
                swap += 1
        return swap

            
        
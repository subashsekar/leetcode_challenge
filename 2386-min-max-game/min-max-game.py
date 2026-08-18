class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return nums[0]
        new_nums = []
        for i in range(len(nums)//2):
            if i % 2 == 0:
                new_nums.append(min(nums[i*2],nums[i*2 + 1]))
            else:
                new_nums.append(max(nums[i*2],nums[i*2 + 1]))
        return self.minMaxGame(new_nums)
               
        
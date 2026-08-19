class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        f = 2
        ans = 2
        for i in range (2, n):
            if nums[i-2] + nums[i-1] == nums[i]:
                f +=1
                ans = max(ans,f)
            else:
                f = 2
        return ans
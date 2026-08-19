class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n-1):
            if nums[i+1] - nums[i] !=1:
                continue
            length = 2
            expected = -1
            for j in range(i+2,n):
                if nums[j] - nums[j-1] !=expected:
                    break
                length +=1
                expected *= -1
            ans = max(ans,length)
        return ans
        
        